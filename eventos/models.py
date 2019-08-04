from django.db import models
import bleach
from gtts import gTTS


# Create your models here.
class Evento(models.Model):
    # Inforamções Principais
    title = models.CharField('Títutlo', max_length=60)
    desc = models.TextField('Descrição')
    local = models.CharField('Local', max_length=60, default='FD, UnB')

    #  Datas
    start_day = models.DateField('Dia em que o Evento começa')
    end_day = models.DateField('Dia em que o Evento Acaba')
    isAllDay = models.BooleanField('É o dia inteiro?')
    start = models.TimeField('Horário de começo')
    end = models.TimeField('Horário de término')

    # Imagem para a página de informações
    show_img = models.ImageField('show_img', default='CADir_logo.png')

    def save(self, *args, **kwargs):
        # Save model atributes
        super(Evento, self).save(*args, **kwargs)

        # Gera áudio apartir das informações
        evento_text = self.title + '.' + self.desc
        evento_text += '.' + ' Local do evento:' + self.local
        if self.start_day == self.end_day:
            evento_text += '.' + ' Dia do evento:' + str(self.start_day)
            if not self.isAllDay:
                evento_text += '.' + ' Começa as ' + str(self.start) + ', Termina as:' + str(self.end)
        else:
            evento_text += '.' + ' Começa dia ' + str(self.start_day) + 'e' + 'termina dia' + str(self.end_day)

        # Text to speech
        tts = gTTS(evento_text, lang='pt-br')
        tts.save('media/audio/eventos/' + str(self.id) + '.mp3')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Eventos'
        verbose_name = 'Evento'
