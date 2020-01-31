from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado, UrlWeb
from .serializers import EmpleadoSerializer, UrlSerializer

class EmpleadoViewSets(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

class UrlViewSets(viewsets.ModelViewSet):
    serializer_class = UrlSerializer
    queryset = UrlWeb.objects.all() 