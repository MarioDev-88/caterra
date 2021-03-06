# Generated by Django 2.2.16 on 2021-03-10 23:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('info_name', models.CharField(max_length=255, verbose_name='Cliente')),
                ('info_business_name', models.CharField(max_length=255, verbose_name='Nombre de la empresa')),
                ('info_address_1', models.CharField(max_length=255, verbose_name='Dirección')),
                ('info_address_2', models.CharField(max_length=255, verbose_name='Colonia')),
                ('info_country', models.CharField(max_length=255, verbose_name='País')),
                ('info_state', models.CharField(max_length=255, verbose_name='Estado')),
                ('info_city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('info_cp', models.CharField(max_length=10, verbose_name='CP')),
                ('info_email', models.EmailField(max_length=255, verbose_name='Email')),
                ('info_phone', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('info_comments', models.TextField(verbose_name='Comentarios')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('DELIVERED', 'DELIVERED'), ('SENT', 'SENT'), ('PAIDOUT', 'PAIDOUT'), ('PENDING', 'PENDING')], max_length=255, verbose_name='Estado del pedido')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20, verbose_name='Admin ID')),
                ('qty', models.IntegerField(verbose_name='Cantidad')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.Order')),
            ],
        ),
    ]
