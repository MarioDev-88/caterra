# Generated by Django 2.2.16 on 2021-03-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210301_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='agentes'),
        ),
        migrations.AlterField(
            model_name='agente',
            name='texto',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
