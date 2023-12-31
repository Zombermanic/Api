from django.db import models

# Create your models here.
class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True, verbose_name = "Id de Usuario")
    Gmail = models.CharField(max_length=50, verbose_name = "Gmail", default=None, null=True)
    password = models.CharField(max_length=50, verbose_name = "Contrasena", default=None, null=True)
    user = models.CharField(max_length=50, verbose_name = "Nombre de Usuario", default=None, null=True)

    def __str__(self):
        return self.user

class Conductor(models.Model):
    idConductor = models.IntegerField(primary_key=True, verbose_name = "Id de Conductor")
    Gmail = models.CharField(max_length=50, verbose_name = "Gmail")
    password = models.CharField(max_length=50, verbose_name = "Contrasena")   
    autoMarca = models.CharField(max_length=50, verbose_name="Marca auto", default=None, null=True)
    autoPatente = models.CharField(max_length=50, verbose_name="Patente auto", default=None, null=True)
    valorViaje = models.IntegerField(verbose_name="Valor viaje", default=None, null=True)
    HoraSalida = models.TimeField(verbose_name="Horas Salida", default=None, null=True)
    user = models.CharField(max_length=50, verbose_name = "Nombre de Conductor")

    def __str__(self):
        return self.user