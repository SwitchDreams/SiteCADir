from django.db import models
from gtts import gTTS
import bleach


# Create your models here.

class Programa(models.Model):
    # Quando alterar tipo choices, atualizar o forms.py
    TIPOS_CHOICES = (
        ('ATL', 'Atlética'),
        ('EJ', 'Empresa Júnior'),
        ('GE', 'Grupos de extensão'),
        ('OUT', 'Outros'),

    )
    # Atributos
    nome = models.CharField('nome', max_length=120, blank=False)
    # Conseguir uma logo default
    logo = models.ImageField('logo', upload_to='programas_logo')
    text = models.TextField('descricao')
    email = models.CharField('email', max_length=120)

    # Tipo(Analisar se vale a pena uma barra de pesquisa via forms ou via js)
    tipo = models.CharField('tipo', max_length=3, choices=TIPOS_CHOICES, default='OUT')

    # Imagem que vai aparecer em cima da descrição
    show_img = models.ImageField('show_img', upload_to='programas_show_img', default='martelo.jpg')

    # Link to social medias
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    site = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    # Audio
    audio = models.FileField(upload_to='media/audio_programas', blank=True)

    def save(self, *args, **kwargs):
        text_clean = bleach.clean(self.text, tags=[],
                                  attributes={},
                                  styles=[],
                                  strip=True)
        text_clean = text_clean.replace('&nbsp;', '')
        print(text_clean)
        tts = gTTS(text_clean, lang='pt-br')
        self.audio = tts.save('media/audio_programas/' + str(self.id) + '.mp3')
        return super(Programa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Programas"
        verbose_name = "Programa"
