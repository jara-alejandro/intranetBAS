""" Url para indicar
los paths """
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import EmpleadoViewSets, UrlViewSets


ROUTER = DefaultRouter()
ROUTER.register('empleados', EmpleadoViewSets)
ROUTER.register('url', UrlViewSets)
urlpatterns = ROUTER.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
