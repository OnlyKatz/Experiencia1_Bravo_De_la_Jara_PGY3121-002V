from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


class Vehiculo(models.Model):
    patente = models.CharField(max_length=5, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

class Formulario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.CharField(max_length=50, primary_key=True, verbose_name='Correo')
    rut = models.CharField(max_length=12, verbose_name='Rut')
    telefono = models.CharField(max_length=15, verbose_name='Telefono')
    ciudad = models.CharField(max_length=20, verbose_name='Ciudad')
    comentario = models.CharField(max_length=250, verbose_name='Comentario')

    def __str__(self):
        return self.correo
    