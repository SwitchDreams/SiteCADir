from django.db import models


# Create your models here.

# Model relacionada a postagens(Estágios, notas)
class Postagem(models.Model):
    nome = models.CharField('Nome', max_length=60, unique=True)
    desc = models.CharField('Descrição', max_length=300, help_text="Descrição abreviada(até 300 caracteres)")

    text = models.TextField('Postagem')

    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"