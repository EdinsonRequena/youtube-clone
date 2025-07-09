from django.conf import settings
from django.db import models


class Like(models.Model):
    """User reaction to a Video: True=like, False=dislike."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    video = models.ForeignKey(
        "videos.Video", on_delete=models.CASCADE, related_name="likes")
    value = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "video")
