from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    registro = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    registro = models.IntegerField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
