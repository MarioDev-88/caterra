import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from tinymce.models import HTMLField
from apps.users.models import Agente


class Slider(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to="static/img/media/sliders", max_length=255)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField("Título del video", max_length=255)
    content = models.TextField("Contenido")
    code = models.TextField("Código del video")

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField("Título", max_length=255)
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

#Modelo imagen
class Image(models.Model):
    # propiedad = models.ForeignKey(Propiedad, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propiedades')

# Propieadad
class Propiedad(models.Model):

    TIPO_INMUEBLE = [
        ('CASA', 'Casa con uso de suelo mixto'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno'),
        ('LOCAL COMERCIAL', 'Local Comercial'),
        ('EDIFICIO', 'Edificio'),
        ('BODEGA', 'Bodega'),
        ('OTRO', 'Otro'),
    ]

    TIPO_OPERACION = [
        ('VENTA', 'Venta'),
        ('RENTA', 'Renta'),
        ('EXCLUSIVA', 'Exclusiva'),
        ('OTRO', 'Otro'),
    ]

    MONEDA = [
        ('MN', 'MN'),
        ('DOLARES', 'Dólares'),
    ]

    ESTADO_CONSERVACION = [
        ('EXCELENTE', 'Excelente'),
        ('MUY BIEN', 'Muy Bien'),
        ('BIEN', 'Bien'),
        ('REGULAR', 'Regular'),
        ('MALO', 'Malo'),
    ]

    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=120)
    # album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
    # imagen = models.ImageField(upload_to="propiedades", null=True, blank=True)
    imagen = models.ForeignKey(Image, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE, null=True, blank=False)
    tipo_operacion = models.CharField(max_length=20, choices=TIPO_OPERACION, null=True, blank=False)
    
    direccion = models.CharField(max_length=200, null=True, blank=False)
    colonia = models.CharField(max_length=100, null=True, blank=False)
    ciudad = models.CharField(max_length=100, null=True, blank=False)
    estado = models.CharField(max_length=100, null=True, blank=False)
    cp = models.CharField(max_length=5, null=True, blank=False)
    entre_calle_1 = models.CharField(max_length=100, null=True, blank=True)
    entre_calle_2 = models.CharField(max_length=100, null=True, blank=True)
    clave = models.CharField(max_length=100, null=True, blank=False)
    captada_por = models.CharField(max_length=100, null=True, blank=False)
    
    construccion = models.CharField(max_length=20, null=True, blank=True)
    terreno = models.CharField(max_length=20, null=True, blank=False)
    frente = models.CharField(max_length=20, null=True, blank=True)
    fondo = models.CharField(max_length=20, null=True, blank=True)
    
    precio = models.CharField(max_length=20, null=True, blank=False)
    moneda = models.CharField(max_length=20, choices=MONEDA, null=True, blank=False)
    mantenimiento_mensual = models.CharField(max_length=20, null=True, blank=True)
    
    cubiculos = models.IntegerField('Cubículos', null=True, blank=True)
    areas_trabajo = models.IntegerField('Áreas de trabajo', null=True, blank=True)
    banos = models.IntegerField('Baños', null=True, blank=True)
    sala_juntas = models.IntegerField('Sala de juntas', null=True, blank=True)
    sala_espera = models.IntegerField('Sala de espera', null=True, blank=True)
    comedor = models.IntegerField(null=True, blank=True)
    cocineta = models.IntegerField(null=True, blank=True)
    lineas_telefonicas = models.IntegerField(null=True, blank=True)
    elevador = models.IntegerField(null=True, blank=True)
    aire_acondicionado = models.IntegerField(null=True, blank=True)
    bodega = models.IntegerField(null=True, blank=True)
    pisos = models.IntegerField(null=True, blank=True)
    canceleria = models.IntegerField(null=True, blank=True)
    garage_descubierto = models.IntegerField(null=True, blank=True)
    garege_cubierto = models.IntegerField(null=True, blank=True)
    estilo = models.CharField(max_length=100, null=True, blank=True)
    niveles = models.IntegerField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    topografia = models.IntegerField(null=True, blank=True)
    forma = models.CharField(max_length=100, null=True, blank=True)
    
    estado_conservacion = models.CharField('Estado de conservación',max_length=20, choices=ESTADO_CONSERVACION, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    instalaciones_especiales = models.CharField(max_length=500, null=True, blank=True)

    #informacion propietario
    prop_nombre = models.CharField(max_length=120, null=True, blank=True)
    prop_direccion = models.CharField(max_length=120, null=True, blank=True)
    prop_colonia = models.CharField(max_length=120, null=True, blank=True)
    prop_cp = models.CharField(max_length=120, null=True, blank=True)
    prop_ciudad = models.CharField(max_length=120, null=True, blank=True)
    prop_telefono = models.CharField(max_length=120, null=True, blank=True)
    prop_cita = models.CharField(max_length=120, null=True, blank=True)
    prop_llaves = models.CharField(max_length=120, null=True, blank=True)
    prop_horario = models.CharField(max_length=120, null=True, blank=True)