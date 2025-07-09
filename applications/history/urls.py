from django.urls import path
from .views import HistoryListView

urlpatterns = [
    path("history/", HistoryListView.as_view(), name="history"),
]
