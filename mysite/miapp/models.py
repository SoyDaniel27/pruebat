from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    decripcion = models.TextField(null=False, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - ${self.decripcion} - ${self.precio} - ${self.disponibilidad}"


