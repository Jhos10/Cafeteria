from django.db import models
from usuarios.models import *
from producto.models import *
# Create your models here.
class Compra(models.Model):
    id_producto = models.ForeignKey(Producto, related_name='producto')
    id_user = models.ForeignKey(User, related_name='usuario')
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    def __str__(self):
        return self.pk
    