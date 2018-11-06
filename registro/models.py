from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.CharField(max_length = 100)
    contra = models.CharField(max_length = 100)
    rut =  models.CharField(max_length = 100)
    nacionalidad =  models.CharField(max_length = 100)
    nombre =  models.CharField(max_length = 100)

class Mensaje(models.Model):
    correo = models.CharField(max_length = 100)    
    orga = models.CharField(max_length = 100)
    mensaje = models.CharField(max_length = 100)
    celu = models.IntegerField()
