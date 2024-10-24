from django.db import models


class Propiedades (models.Model):
    metros_cuadrados = models.IntegerField ()
    ubicacion = models.CharField (max_length=20)
    precio = models.CharField (max_length=20)

    def __str__(self):
        return f"{self.precio} {self.ubicacion} {self.metros_cuadrados}"  