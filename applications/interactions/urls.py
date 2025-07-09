from django.urls import path
from .views import LikeToggleView

urlpatterns = [
    path("videos/<int:pk>/react/", LikeToggleView.as_view(), name="video-react"),
]
