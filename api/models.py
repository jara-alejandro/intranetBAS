from django.db import models


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    fecha_nac = models.DateField()

    class Meta:
        managed = False
        db_table = 'empleado'


class UrlWeb(models.Model):
    id_url = models.AutoField(primary_key=True)
    url = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'url_web'
    def __str__(self):
        return self.descripcion
