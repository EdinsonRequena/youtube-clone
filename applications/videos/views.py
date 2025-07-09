from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Video
from .forms import VideoForm
from comments.forms import CommentForm

from history.models import WatchEvent

from django.db.models.functions import Now, Extract
from django.db.models import (
    Count,
    Q,
    F,
    IntegerField,
    ExpressionWrapper,
    DurationField,
    Value
)


class VideoListView(ListView):
    template_name = "videos/home.html"
    model = Video
    context_object_name = "videos"
    paginate_by = 10


class VideoDetailView(DetailView):
    template_name = "videos/detail.html"
    model = Video
    context_object_name = "video"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if request.user.is_authenticated:
            WatchEvent.objects.create(user=request.user, video=self.object)

        return response

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        video = self.object
        ctx.update({
            "likes": video.likes.filter(value=True).count(),
            "dislikes": video.likes.filter(value=False).count(),
            "comments": video.comments.select_related("user"),
            "comment_form": CommentForm(),
        })
        if self.request.user.is_authenticated:
            user_like = video.likes.filter(user=self.request.user).first()
            ctx["user_reaction"] = (
                "like" if user_like and user_like.value else
                "dislike" if user_like and not user_like.value else
                "none"
            )
        return ctx


class VideoCreateView(LoginRequiredMixin, CreateView):
    template_name = "videos/create.html"
    form_class = VideoForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PopularListView(ListView):
    template_name = "videos/popular.html"
    model = Video
    context_object_name = "videos"

    def get_queryset(self):
        today = date.today()

        qs = (
            Video.objects
            .annotate(
                likes_cnt=Count("likes", filter=Q(likes__value=True)),
                dislikes_cnt=Count("likes", filter=Q(likes__value=False)),
                comments_cnt=Count("comments"),
            )
        )

        qs = qs.annotate(
            age=ExpressionWrapper(Now() - F("created_at"),
                                  output_field=DurationField())
        ).annotate(
            days_ago=Extract("age", "day")
        )

        qs = qs.annotate(
            recency_pts=ExpressionWrapper(
                (Value(1) - F("days_ago")) * 100,
                output_field=IntegerField(),
            )
        )

        qs = qs.annotate(
            popularity=(
                F("likes_cnt") * 10 +
                F("dislikes_cnt") * -5 +
                F("comments_cnt") +
                F("recency_pts")
            )
        )

        qs_month = qs.filter(
            created_at__year=today.year,
            created_at__month=today.month,
        )
        return (qs_month or qs).order_by("-popularity")[:5]
