from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("title", "embed_url")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "embed_url": forms.URLInput(attrs={"class": "form-control"}),
        }
