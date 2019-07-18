from django.db import models


# Create your models here.

class Categoria(models.Model):
    # Nome da Categoria
    nome = models.CharField('nome', max_length=60)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class MensagemOuvidoria(models.Model):
    # Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Data
    data = models.DateField(auto_now_add=True)
