# Generated by Django 4.0.4 on 2022-06-01 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca Vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]