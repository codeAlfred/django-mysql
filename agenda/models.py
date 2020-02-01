from django.db import models

# Create your models here.
class agenda(models.Model):
    nombre=models.CharField(max_length=88)
    apellido_paterno=models.CharField(max_length=99)
    apellido_materno=models.CharField(max_length=99)

class producto(models.Model):
    nombre=models.CharField(max_length=88)
    precio=models.IntegerField(default=1)
    marca=models.CharField(max_length=99)
    stock=models.IntegerField(default=100)

class cliente(models.Model):
    nombre=models.CharField(max_length=88)
    apellido_paterno=models.CharField(max_length=99)
    apellido_materno=models.CharField(max_length=99)
    email=models.EmailField(max_length=100)
    fecha_registro=models.DateTimeField('date published')
    edad=models.IntegerField(default=18)
    direccion=models.TextField(default='Lima - Perú')