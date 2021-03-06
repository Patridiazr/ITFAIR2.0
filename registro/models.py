from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.CharField(max_length = 100)
    contra = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)    
    nacionalidad =  models.CharField(max_length = 100)
    

class Mensaje(models.Model):
    nombre = models.CharField(max_length = 100)
    correo = models.CharField(max_length = 100)
    mensaje = models.CharField(max_length = 100)
    telefono = models.IntegerField()
    


class Turistico(models.Model):
    titulo = models.CharField(max_length = 100)    
    subtitulo = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to='fotos/')
    descripcion = models.CharField(max_length = 1500)    

class Servicios(models.Model):
    nombre = models.CharField(max_length = 100) 
    titulo = models.CharField(max_length = 100)    
    archivo = models.FileField(upload_to='archivos/')    
    downl = models.CharField(max_length = 100)    
    descripcion = models.CharField(max_length = 100)


