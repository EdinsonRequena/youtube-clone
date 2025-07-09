from django.urls import path
from .views import CommentCreateView

urlpatterns = [
    path("videos/<int:pk>/comment/",
         CommentCreateView.as_view(), name="comment-create"),
]
