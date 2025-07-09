from django.urls import path
from .views import VideoListView, VideoDetailView, VideoCreateView, PopularListView

urlpatterns = [
    path("", VideoListView.as_view(), name="home"),
    path("popular/", PopularListView.as_view(), name="popular"),
    path("videos/new/", VideoCreateView.as_view(), name="video-create"),
    path("videos/<int:pk>/", VideoDetailView.as_view(), name="video-detail"),
]
