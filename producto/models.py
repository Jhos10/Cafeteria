from django.db import models


class Producto_cateogoria(models.Model):
    nombre_categoria = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre_categoria

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=80)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    id_categoria = models.ForeignKey(Producto_cateogoria, related_name='producto_categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_producto