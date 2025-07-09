from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("video", "user", "created_at", "short_text")
    search_fields = ("video__title", "user__username", "text")
    autocomplete_fields = ("video", "user")

    def short_text(self, obj):
        return obj.text[:50] + ("…" if len(obj.text) > 50 else "")
