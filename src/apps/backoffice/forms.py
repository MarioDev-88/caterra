from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Slider, Video, Post, Propiedad
from apps.users.models import Agente


class AgenteChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.user.first_surname, obj.user.first_name)


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

class PropiedadForm(forms.ModelForm):

    agente = AgenteChoiceField(queryset = Agente.objects.all())        

    class Meta:
        model = Propiedad
        fields = ('__all__')