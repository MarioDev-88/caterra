from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Slider, Video, Post, Propiedad, Image
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

        widgets = {
            'nombre': forms.TextInput(
                attrs={                
                    'placeholder' : 'Nombre de la propiedad *',                
                }
            ),
            'tipo_inmueble': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
            'tipo_operacion': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
            'direccion': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Dirección *',
                }
            ),
            'colonia': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Colonia *',
                }
            ),
            'ciudad': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Ciudad *',
                }
            ),
            'estado': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Estado *',
                }
            ),
            'cp': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Código Postal *',
                }
            ),
            'entre_calle_1': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Entre calle *',
                }
            ),
            'entre_calle_2': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Y calle *',
                }
            ),
            'clave': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Clave *',
                }
            ),
            'captada_por': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Captado por *',
                }
            ),
            'construccion': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Construcción *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon',
                }
            ),
            'terreno': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Terreno *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon',
                }
            ),
            'frente': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Frente *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon',
                }
            ),
            'fondo': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Fondo *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon',
                }
            ),
            'precio': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Precio *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon2',
                }
            ),
            'moneda': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
            'mantenimiento_mensual': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Mantenimineto mensual *',
                    'class' : 'form-control',
                    'aria-describedby' : 'basic-addon',
                }
            ),
            'estado_conservacion': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
            'observaciones': forms.Textarea(
                attrs={ 
                    'placeholder' : 'Escribe observaciones de la propiedad aquí...',
                    'class' : 'form-control',
                }
            ),
            'instalaciones_especiales': forms.Textarea(
                attrs={ 
                    'placeholder' : 'Instalaciones especiales',
                    'class' : 'form-control',
                }
            ),
            'prop_nombre': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Nombre del propietario',
                    'class' : 'form-control',
                }
            ),
            'prop_direccion': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Dirección',
                    'class' : 'form-control',
                }
            ),
            'prop_colonia': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Colonia',
                    'class' : 'form-control',
                }
            ),
            'prop_cp': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Código Postal',
                    'class' : 'form-control',
                }
            ),
            'prop_ciudad': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Ciudad',
                    'class' : 'form-control',
                }
            ),
            'prop_telefono': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Teléfono',
                    'class' : 'form-control',
                }
            ),
            'prop_cita': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Cita',
                    'class' : 'form-control',
                }
            ),
            'prop_llaves': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Llaves',
                    'class' : 'form-control',
                }
            ),
            'prop_horario': forms.TextInput(
                attrs={ 
                    'placeholder' : 'Horario',
                    'class' : 'form-control',
                }
            ),
        }

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)