
""""
Serializador para las clases que vienen de la base de datos. Con esto armo el
JSON
"""
from rest_framework import serializers
from .models import Empleado, UrlWeb


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlWeb
        fields = '__all__'
