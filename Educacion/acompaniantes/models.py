from django.db import models

class Acompaniante(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

