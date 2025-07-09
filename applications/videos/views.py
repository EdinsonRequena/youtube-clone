from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Video
from .forms import VideoForm


class VideoListView(ListView):
    template_name = "videos/home.html"
    model = Video
    context_object_name = "videos"
    paginate_by = 10


class VideoDetailView(DetailView):
    template_name = "videos/detail.html"
    model = Video
    context_object_name = "video"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        video = self.object
        ctx["likes"] = video.likes.filter(value=True).count()
        ctx["dislikes"] = video.likes.filter(value=False).count()
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
