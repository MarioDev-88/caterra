# Generated by Django 2.2.16 on 2021-05-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(max_length=255, upload_to='sliders'),
        ),
    ]
