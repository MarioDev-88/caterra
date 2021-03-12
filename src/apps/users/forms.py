from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

from .models import User, Agente




class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label="Confirmación de contraseña", 
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirmación de contraseña'
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "first_surname", "last_surname", "email", "phone", "type")

        widgets = {
            'first_name': forms.TextInput(
                attrs={                
                    'placeholder' : 'Nombre',                
                }
            ),
            'first_surname': forms.TextInput(
                attrs={                
                    'placeholder' : 'Primer apellido',                
                }
            ),
            'last_surname': forms.TextInput(
                attrs={               
                    'placeholder' : 'Segundo apellido',                
                }
            ),
            'email': forms.TextInput(
                attrs={               
                    'placeholder' : 'Correo',                
                }
            ),
            'phone': forms.TextInput(
                attrs={   
                    'id' : 'phone-mask',   
                    'class' : 'phone-inputmask',
                    'placeholder' : 'Teléfono',                
                }
            ),
            'type': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
        }

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password1

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label="Contraseña",
        help_text=""" Raw passwords are not stored, so there is no way to see this user's password,
            but you can change the password using <a href='../password/'>this form</a>. """,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "first_surname",
            "last_surname",
            "email",
            "phone",
            "type",
            "password",
        )

        widgets = {
            'first_name': forms.TextInput(
                attrs={                
                    'placeholder' : 'Nombre',                
                }
            ),
            'first_surname': forms.TextInput(
                attrs={                
                    'placeholder' : 'Primer apellido',                
                }
            ),
            'last_surname': forms.TextInput(
                attrs={               
                    'placeholder' : 'Segundo apellido',                
                }
            ),
            'email': forms.TextInput(
                attrs={               
                    'placeholder' : 'Correo',                
                }
            ),
            'phone': forms.TextInput(
                attrs={   
                    'id' : 'phone-mask',   
                    'class' : 'phone-inputmask',
                    'placeholder' : 'Teléfono',                
                }
            ),
            'type': forms.Select(
                attrs={ 
                    'class' : 'select2 form-control custom-select',
                }
            ),
        }

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", required=True, widget=forms.EmailInput())
    password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput())


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "first_surname",
            "last_surname",
            "phone",
            "email",
            "type",
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "first_surname",
            "phone",
            "email",
        )


class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ('foto', 'texto')

        widgets = {
            'texto': forms.Textarea(
                attrs={                
                    'placeholder' : 'Escribe tu mensaje aquí...',                
                }
            ),
        }

        # def __init__(self, *args, **kwargs):
        #     super(AgenteForm, self).__init__(*args, **kwargs)
        #     self.fields['foto'].required = False
        #     self.fields['texto'].required = False

class AgenteUpdateForm(forms.ModelForm):
        class Meta:
            model = Agente
            fields = ('foto', 'texto')

            widgets = {
                'texto': forms.Textarea(
                    attrs={                
                        'placeholder' : 'Escribe tu mensaje aquí...',                
                    }
                ),
            }

            # def save(self, user, commit=True):
            #     instance = super(AgenteUpdateForm, self).save(commit=False)
            #     print('***************************')
            #     print(instance)
            #     print(instance.user)
            #     if not self.instance.pk:
            #         if commit:
            #             instance.user = user
            #             instance.save()
            #     return instance