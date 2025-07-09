from django.urls import reverse
from history.models import WatchEvent


def test_history_shows_only_user_events(client_logged, user, make_user, video_factory):
    v1 = video_factory("V1")
    v2 = video_factory("V2")

    WatchEvent.objects.create(user=user, video=v1)
    WatchEvent.objects.create(user=make_user(), video=v2)

    resp = client_logged.get(reverse("history"))
    events = resp.context["events"]

    assert events.count() == 1 and events[0].video == v1
