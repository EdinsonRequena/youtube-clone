from django.urls import path
from .views import VideoListView, VideoDetailView, VideoCreateView

urlpatterns = [
    path("", VideoListView.as_view(), name="home"),
    path("videos/new/", VideoCreateView.as_view(), name="video-create"),
    path("videos/<int:pk>/", VideoDetailView.as_view(), name="video-detail"),
]
