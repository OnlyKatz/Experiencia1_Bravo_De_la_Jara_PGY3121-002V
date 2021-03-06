# Generated by Django 4.0.4 on 2022-06-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo')),
                ('rut', models.CharField(max_length=12, verbose_name='Rut')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad')),
                ('comentario', models.CharField(max_length=250, verbose_name='Comentario')),
            ],
        ),
    ]
