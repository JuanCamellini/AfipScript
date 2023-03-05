from django.db import models

# Create your models here.
class Paciente(models.Model):
    tipo_factura = models.CharField(max_length=100)
    cuit = models.CharField(max_length=1000)
    detalle_servicio = models.CharField(max_length=400)
    cantidad_sesiones = models.CharField(max_length=50)
    precio_unitario = models.CharField(max_length=50)
    iva = models.CharField(max_length=200)
    dni = models.IntegerField(max_length=55000000)
    nombre = models.CharField(max_length=1300)
    obra_social = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return f"{self.nombre} ({self.dni})"