from datetime import timedelta
import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from videos.models import Video

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="alice", password="pass")


@pytest.fixture
def client_logged(client, user):
    client.login(username="alice", password="pass")
    return client


@pytest.fixture
def make_user(db):
    counter = {"n": 0}

    def _new(prefix="u"):
        counter["n"] += 1
        return User.objects.create_user(
            username=f"{prefix}{counter['n']}",
            password="pass",
        )
    return _new


@pytest.fixture
def video_factory(db, user):
    def _make(title, days_offset=0, owner=None):
        return Video.objects.create(
            title=title,
            embed_url="https://www.youtube.com/embed/dQw4w9WgXcQ",
            owner=owner or user,
            created_at=timezone.now() + timedelta(days=days_offset),
        )
    return _make
