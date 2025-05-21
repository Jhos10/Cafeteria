from rest_framework import serializers
from .models import Producto, Producto_cateogoria

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ProductoCategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto_cateogoria
        fields = "__all__"

