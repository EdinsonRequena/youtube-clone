from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views import View

from videos.models import Video
from .models import Like


class LikeToggleView(LoginRequiredMixin, View):
    """
    Toggle the like or dislike status for a video via an AJAX POST request.

    This view handles the toggling of a "like" or "dislike" action for a video
    by the authenticated user. If the user has already liked or disliked the video,
    the action will be reversed or updated based on the provided value.

    Attributes:
        LoginRequiredMixin: Ensures the user is authenticated before accessing the view.
        View: Base class for handling HTTP requests.

    Methods:
        post(request, pk):
            Handles the AJAX POST request to toggle the like/dislike status.
            Args:
                request: The HTTP request object containing POST data.
                pk: The primary key of the video to toggle the like/dislike status for.
            Returns:
                JsonResponse: A JSON response containing the updated counts of likes,
                              dislikes, and the user's current like/dislike status.
    """

    def post(self, request, pk):
        """
        Handle POST requests to like or dislike a video.

        Args:
            request (HttpRequest): The HTTP request object containing user and POST data.
            pk (int): The primary key of the video to be liked or disliked.

        Returns:
            JsonResponse: A JSON response containing the updated counts of likes, dislikes,
                          and the user's current interaction value ("like", "dislike", or "none").
            HttpResponseBadRequest: If the provided value is invalid (not "like" or "dislike").

        Behavior:
            - Retrieves the video object using the provided primary key.
            - Validates the "value" parameter from the POST data to ensure it is either "like" or "dislike".
            - Creates or updates the Like object for the user and video based on the provided value.
            - Deletes the Like object if the user toggles the same value again.
            - Calculates the total counts of likes and dislikes for the video.
            - Determines the user's current interaction value with the video.
        """
        video = get_object_or_404(Video, pk=pk)
        value = request.POST.get("value")
        if value not in ("like", "dislike"):
            return HttpResponseBadRequest("Invalid value")

        value_bool = value == "like"

        like_obj, created = Like.objects.get_or_create(user=request.user, video=video,
                                                       defaults={"value": value_bool})
        if not created:
            if like_obj.value == value_bool:
                like_obj.delete()
            else:
                like_obj.value = value_bool
                like_obj.save()

        likes = video.likes.filter(value=True).count()
        dislikes = video.likes.filter(value=False).count()
        user_val = (
            "like" if like_obj.value and like_obj.pk else
            "dislike" if like_obj.pk and not like_obj.value else
            "none"
        )

        return JsonResponse({"likes": likes, "dislikes": dislikes, "user_value": user_val})
