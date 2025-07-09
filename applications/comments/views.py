from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import CommentForm
from videos.models import Video


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        video = Video.objects.get(pk=self.kwargs["pk"])
        form.instance.user = self.request.user
        form.instance.video = video
        form.save()
        return HttpResponseRedirect(reverse("video-detail", args=[video.pk]))
