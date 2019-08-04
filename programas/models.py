from django.db import models
from gtts import gTTS
import bleach
from django.conf import settings

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

    def tts(self):
        # Clean text
        text_clean = bleach.clean(self.text, tags=[],
                                  attributes={},
                                  styles=[],
                                  strip=True)
        text_clean = text_clean.replace('&nbsp;', '')

        # Text to speech
        tts = gTTS(text_clean, lang='pt-br')
        tts.save( settings.MEDIA_ROOT + 'audio/programas/' + str(self.id) + '.mp3')

    def save(self, *args, **kwargs):
        # Se não for a primeira vez
        if not self.pk:
            super(Programa, self).save(*args, **kwargs)
            self.tts()
        else:
            old = Programa.objects.filter(pk=self.pk).first()
            texto_anterior = old.text
            super(Programa, self).save(*args, **kwargs)
            # Verifica se o texto foi alterado para gerar um novo áudio
            if texto_anterior != self.text:
                self.tts()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Programas"
        verbose_name = "Programa"
