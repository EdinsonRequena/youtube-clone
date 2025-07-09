from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model ready for future fields (avatar, bio, etc.)."""
    # avatar = models.ImageField(upload_to="avatars/", blank=True)
