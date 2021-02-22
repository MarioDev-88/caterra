from django import forms

from .models import Slider, Video, MonthOffer, Post


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ["title", "url", "image", "order"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "content", "code"]


class MonthOfferForm(forms.ModelForm):
    class Meta:
        model = MonthOffer
        fields = ["title", "admintotal_id", "description", "price", "image", "discount"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content", "header"]
