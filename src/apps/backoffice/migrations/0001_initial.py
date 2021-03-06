# Generated by Django 2.2.16 on 2021-03-12 19:40

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='propiedades')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('image', models.ImageField(upload_to='posts', verbose_name='Imagen')),
                ('header', models.ImageField(upload_to='posts_headers', verbose_name='Header')),
                ('content', tinymce.models.HTMLField(verbose_name='Contenido')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, upload_to='static/img/media/sliders')),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título del video')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('code', models.TextField(verbose_name='Código del video')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('tipo_inmueble', models.CharField(choices=[('CASA', 'Casa con uso de suelo mixto'), ('OFICINA', 'Oficina'), ('TERRENO', 'Terreno'), ('LOCAL COMERCIAL', 'Local Comercial'), ('EDIFICIO', 'Edificio'), ('BODEGA', 'Bodega'), ('OTRO', 'Otro')], max_length=20, null=True)),
                ('tipo_operacion', models.CharField(choices=[('VENTA', 'Venta'), ('RENTA', 'Renta'), ('EXCLUSIVA', 'Exclusiva'), ('OTRO', 'Otro')], max_length=20, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('colonia', models.CharField(max_length=100, null=True)),
                ('ciudad', models.CharField(max_length=100, null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
                ('cp', models.CharField(max_length=5, null=True)),
                ('entre_calle_1', models.CharField(blank=True, max_length=100, null=True)),
                ('entre_calle_2', models.CharField(blank=True, max_length=100, null=True)),
                ('clave', models.CharField(max_length=100, null=True)),
                ('captada_por', models.CharField(max_length=100, null=True)),
                ('construccion', models.CharField(blank=True, max_length=20, null=True)),
                ('terreno', models.CharField(max_length=20, null=True)),
                ('frente', models.CharField(blank=True, max_length=20, null=True)),
                ('fondo', models.CharField(blank=True, max_length=20, null=True)),
                ('precio', models.CharField(max_length=20, null=True)),
                ('moneda', models.CharField(choices=[('MN', 'MN'), ('DOLARES', 'Dólares')], max_length=20, null=True)),
                ('mantenimiento_mensual', models.CharField(blank=True, max_length=20, null=True)),
                ('cubiculos', models.IntegerField(blank=True, null=True, verbose_name='Cubículos')),
                ('areas_trabajo', models.IntegerField(blank=True, null=True, verbose_name='Áreas de trabajo')),
                ('banos', models.IntegerField(blank=True, null=True, verbose_name='Baños')),
                ('sala_juntas', models.IntegerField(blank=True, null=True, verbose_name='Sala de juntas')),
                ('sala_espera', models.IntegerField(blank=True, null=True, verbose_name='Sala de espera')),
                ('comedor', models.IntegerField(blank=True, null=True)),
                ('cocineta', models.IntegerField(blank=True, null=True)),
                ('lineas_telefonicas', models.IntegerField(blank=True, null=True)),
                ('elevador', models.IntegerField(blank=True, null=True)),
                ('aire_acondicionado', models.IntegerField(blank=True, null=True)),
                ('bodega', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('canceleria', models.IntegerField(blank=True, null=True)),
                ('garage_descubierto', models.IntegerField(blank=True, null=True)),
                ('garage_cubierto', models.IntegerField(blank=True, null=True)),
                ('estilo', models.CharField(blank=True, max_length=100, null=True)),
                ('niveles', models.IntegerField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('topografia', models.IntegerField(blank=True, null=True)),
                ('forma', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_conservacion', models.CharField(blank=True, choices=[('EXCELENTE', 'Excelente'), ('MUY BIEN', 'Muy Bien'), ('BIEN', 'Bien'), ('REGULAR', 'Regular'), ('MALO', 'Malo')], max_length=20, null=True, verbose_name='Estado de conservación')),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('instalaciones_especiales', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('prop_nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_direccion', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_colonia', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_cp', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_ciudad', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_telefono', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_cita', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_llaves', models.CharField(blank=True, max_length=120, null=True)),
                ('prop_horario', models.CharField(blank=True, max_length=120, null=True)),
                ('agente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Agente')),
                ('imagen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backoffice.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backoffice.Post')),
            ],
        ),
    ]
