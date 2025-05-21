from django.contrib import admin
from .models import *
# Register your models here.
class CompraAdmin(admin.ModelAdmin):
    model = Compra


# Va a utilizar la compra en la base de datos para hacer el compra admin
admin.site.register(Compra, CompraAdmin)