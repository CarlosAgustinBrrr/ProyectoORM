from django.db import models

# Create your models here.

class TipoCoche(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class MarcaCoche(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Coche(models.Model):
    tipo_coche = models.ForeignKey(TipoCoche, on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcaCoche, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    puertas = models.IntegerField()