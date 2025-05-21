from rest_framework import serializers
from .models import Compra

class CompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

    


