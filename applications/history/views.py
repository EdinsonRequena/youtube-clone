from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import WatchEvent


class HistoryListView(LoginRequiredMixin, ListView):
    template_name = "history/list.html"
    model = WatchEvent
    context_object_name = "events"
    paginate_by = 20

    def get_queryset(self):
        return (
            WatchEvent.objects
            .filter(user=self.request.user)
            .select_related("video")
        )
