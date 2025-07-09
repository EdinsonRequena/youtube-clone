from django.contrib import admin
from .models import WatchEvent


@admin.register(WatchEvent)
class WatchEventAdmin(admin.ModelAdmin):
    list_display = ("video", "user", "watched_at")
    search_fields = ("video__title", "user__username")
    autocomplete_fields = ("video", "user")
