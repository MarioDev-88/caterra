# Generated by Django 2.2.16 on 2021-03-11 22:56

import apps.users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('first_surname', models.CharField(max_length=255, verbose_name='Primer apellido')),
                ('last_surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Segundo apellido')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('type', models.CharField(choices=[('ADMIN', 'Admin'), ('AGENTE', 'Agente'), ('EDITOR', 'Editor'), ('CLIENTE', 'Cliente')], max_length=20, verbose_name='Tipo')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Actualizado')),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='agentes')),
                ('texto', models.TextField(max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
    ]
