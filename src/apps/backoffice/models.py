import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from tinymce.models import HTMLField


class Slider(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to="sliders", max_length=255)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField("Titulo del video", max_length=255)
    content = models.TextField("Contenido")
    code = models.TextField("Código del video")

    def __str__(self):
        return self.title


class MonthOffer(models.Model):
    title = models.CharField("Titulo", max_length=255)
    admintotal_id = models.CharField("AdminTotal ID", max_length=50)
    description = models.CharField("Descripción", max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField("Imagen", upload_to="offers")
    discount = models.DecimalField("Descuento", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField("Titulo", max_length=255)
    image = models.ImageField("Imagen", upload_to="posts")
    header = models.ImageField("Header", upload_to="posts_headers")
    content = HTMLField("Contenido")
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.title


def set_slug(sender, instance, *args, **kwargs):
    id = str(uuid.uuid4())
    instance.slug = slugify("{}-{}".format(instance.title, id[:8]))


pre_save.connect(set_slug, sender=Post)


class Comment(models.Model):
    name = models.CharField('Nombre', max_length=255)
    email = models.EmailField('Correo electrónico', max_length=255)
    content = models.TextField('Contenido')
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    created_at = models.DateField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.email
