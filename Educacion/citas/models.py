from django.db import models
from acompaniantes.models import Acompaniante

class Cita(models.Model):
    acompaniante = models.ForeignKey(Acompaniante, on_delete=models.CASCADE, default=None)
    fecha = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.fecha, self.hora)