from rest_framework import serializers
from .models import Producto
# Name the class as (model name + 'Serializer')


class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
