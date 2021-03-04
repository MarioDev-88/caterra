from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, first_surname, email, password, *args, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name, first_surname=first_surname, email=email, *args, **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, first_surname, email, password, *args, **kwargs):
        kwargs["is_superuser"] = True
        kwargs["is_staff"] = True
        kwargs["type"] = "ADMIN"

        return self._create_user(first_name, first_surname, email, password, *args, **kwargs)

    def create_user(self, first_name, first_surname, email, password=None, *args, **kwargs):
        kwargs["is_superuser"] = False

        return self._create_user(first_name, first_surname, email, password, *args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = [
        ("ADMIN", "Admin"),
        ("AGENTE", "Agente"),
        ("EDITOR", "Editor"),
        ("CLIENTE", "Cliente"),
    ]

    first_name = models.CharField("Nombre", max_length=255)
    first_surname = models.CharField("Primer apellido", max_length=255)
    last_surname = models.CharField("Segundo apellido", max_length=255, blank=True, null=True)
    email = models.EmailField("Correo electrónico", max_length=255, unique=True)
    phone = models.CharField("Telefono", max_length=50, blank=True, null=True)
    type = models.CharField("Tipo", max_length=20, choices=USER_TYPES)
    created_at = models.DateField("Creado", auto_now_add=True)
    updated_at = models.DateField("Actualizado", auto_now=True)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "first_surname"]

    def __str__(self):
        return "{} {}".format(self.first_name, self.first_surname)


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(type="ADMIN")


class EditorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(type="EDITOR")


class ClienteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(type="CLIENTE")


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True


class Editor(User):
    objects = EditorManager()

    class Meta:
        proxy = True


class Cliente(User):
    objects = ClienteManager()

    class Meta:
        proxy = True


class Agente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="agentes", null=True, blank=True)
    texto = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.first_surname)