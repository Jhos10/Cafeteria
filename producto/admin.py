from django.contrib import admin
from .models import Producto, Producto_cateogoria
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    model=Producto

class ProductoCategoriaAdmin(admin.ModelAdmin):
    model= Producto_cateogoria
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Producto_cateogoria,ProductoCategoriaAdmin)
