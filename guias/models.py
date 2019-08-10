from django.db import models


# Create your models here.
class Guia(models.Model):
    # Nome do guia
    nome = models.CharField('Nome', max_length=60)
    # Descrição do guia
    desc = models.TextField('Descrição', default='Guia CADir UnB')
    # Duração da leitura
    duracao = models.IntegerField('Duração de leitura', default=30, help_text='Colocar a duração em minutos')
    # Link para guia externo
    link = models.URLField('Link', blank=True)
    # File para dowload
    file = models.FileField('Arquivo', upload_to='guias_pdf', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Guias"
        verbose_name = "Guia"
