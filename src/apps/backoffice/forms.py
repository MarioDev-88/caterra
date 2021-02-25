from django import forms

from .models import Slider, Video, Post, Propiedad


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ["title", "url", "image", "order"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "content", "code"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content", "header"]

class CrearPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ('__all__')