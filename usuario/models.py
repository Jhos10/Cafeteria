from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    es_admin = models.BooleanField(default=False)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=80, unique=True)