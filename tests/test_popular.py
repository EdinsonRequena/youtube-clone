from django.urls import reverse
from freezegun import freeze_time
from interactions.models import Like
from comments.models import Comment


@freeze_time("2025-07-09")
def test_popular_ranking(client_logged, user, make_user, video_factory):
    a = video_factory("A")
    for _ in range(3):
        Like.objects.create(user=make_user(), video=a, value=True)
    Comment.objects.create(user=user, video=a, text="nice")

    b = video_factory("B", days_offset=-3)
    for _ in range(4):
        Like.objects.create(user=make_user(), video=b, value=True)

    resp = client_logged.get(reverse("popular"))
    videos = list(resp.context["videos"])

    scores = [v.popularity for v in videos]
    assert scores == sorted(scores, reverse=True)

    assert videos[0].popularity > videos[1].popularity
