from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    # Imagen
    imagen = models.FileField(upload_to='imagenes/productos/')
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
