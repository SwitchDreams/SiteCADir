from django.db import models


# Create your models here.
class Evento(models.Model):

    # Inforamções Principais
    title = models.CharField('Títutlo', max_length=60)
    desc = models.TextField('Descrição')
    #  Datas
    day = models.DateField('Dia')
    isAllDay = models.BooleanField('É o dia inteiro?')
    start = models.TimeField('Horário de começo')
    end = models.TimeField('Horário de término')
    #  Link para mais informações
    link = models.URLField('link', blank=True)
