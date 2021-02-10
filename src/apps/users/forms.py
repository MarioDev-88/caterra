from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

from .models import User


class CustomUserCreationForm(UserCreationForm):

    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmación de contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "first_surname", "last_surname", "email", "password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords doen't match.")

        return password

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

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
            "password",
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
            "password",
        )
