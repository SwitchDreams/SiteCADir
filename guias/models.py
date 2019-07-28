from django.db import models

# Create your models here.
class Guia(models.Model):

    # Link para guia externo
    link = models.URLField('Link')

    class Meta:
        verbose_name_plural = "Guias"
        verbose_name = "Guia"