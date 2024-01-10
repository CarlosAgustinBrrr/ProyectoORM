from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True)
    nombre_modelo = models.CharField(max_length=255)
    numero_puertas = models.IntegerField()
    tipo_motor = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_modelo

class Vehiculo(models.Model):
    idVehiculo = models.AutoField(primary_key=True)
    idmarca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    idmodelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.idmarca} - {self.idmodelo} - {self.color}"
