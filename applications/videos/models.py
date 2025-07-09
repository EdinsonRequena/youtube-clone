from django.conf import settings
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    embed_url = models.URLField(
        help_text="YouTube embed URL (https://www.youtube.com/embed/...)")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="videos")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.title)
