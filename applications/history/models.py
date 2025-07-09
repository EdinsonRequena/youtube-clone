from django.conf import settings
from django.db import models


class WatchEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    video = models.ForeignKey("videos.Video", on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-watched_at",)

    def __str__(self):
        return f"{self.user} → {self.video} @ {self.watched_at:%Y-%m-%d %H:%M}"
