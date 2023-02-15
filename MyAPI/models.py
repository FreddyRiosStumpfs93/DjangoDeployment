from django.db import models

# Create your models here.
class clasificacion(models.Model):
    MATERIALES = (
        ('Plastico', 'Plastico'),
        ('Vidrio', 'Vidrio'),
        ('Ceramica', 'Ceramica')
    )
    descripcion = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIALES)

    def __str__(self):
        return self.descripcion
