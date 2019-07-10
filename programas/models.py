from django.db import models

# Create your models here.

class Programa(models.Model):
    TIPOS_CHOICES = (
        ('ATL', 'Atlética'),
        ('EJ', 'Empresa Junior'),
        ('GE', 'Grupo de extensão'),
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

    # Link to social medias
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    site = models.URLField(blank=True)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Programas"
        verbose_name = "Programa"