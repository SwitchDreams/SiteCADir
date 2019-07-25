from django.db import models


# Create your models here.
class Evento(models.Model):

    # Inforamções Principais
    title = models.CharField('Títutlo', max_length=60)
    desc = models.TextField('Descrição')
    local = models.CharField('Local', max_length=60, default='FD, UnB')

    #  Datas
    day = models.DateField('Dia')
    isAllDay = models.BooleanField('É o dia inteiro?')
    start = models.TimeField('Horário de começo')
    end = models.TimeField('Horário de término')

    # Imagem para a página de informações
    show_img = models.ImageField('show_img', default='CADir_logo.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Eventos'
        verbose_name = 'Evento'