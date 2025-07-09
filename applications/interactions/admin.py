from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("video", "user", "value", "created_at")
    list_filter = ("value",)
    autocomplete_fields = ("video", "user")
