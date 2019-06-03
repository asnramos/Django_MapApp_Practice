from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    location =  models.PointField(srid=4326, verbose_name='Ubicación')
    objects = models.Manager()
    
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        ordering = ['created']

    def __str__(self):
            return self.name