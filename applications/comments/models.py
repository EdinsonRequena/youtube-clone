from django.conf import settings
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    video = models.ForeignKey(
        "videos.Video", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user}: {self.text[:40]}..."
