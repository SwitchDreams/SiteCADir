from django.core.exceptions import ValidationError
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

# Model relacionada as prestações de conta
class PrestacaoDeContas(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome que aparecerá no site(Institucional)')
    # File para dowload
    file = models.FileField('Arquivo', upload_to='prestacao_de_contas_pdf')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Prestações de Conta"
        verbose_name = "Prestação de conta"

# Model relacionada as prestações de conta
class Atas(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome que aparecerá no site(Institucional)')
    # File para dowload
    file = models.FileField('Arquivo', upload_to='atas_pdf')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Atas"
        verbose_name = "Ata"

# Model relacionada ao Texto do histórico do CADir
class TextoHistorico(models.Model):
    texto = models.TextField('Texto', help_text='Texto no qual se encontra no ver mais do histórico do CADir')

    def __str__(self):
        return "Texto do histórico do CADir"

    def save(self, *args, **kwargs):
        if TextoHistorico.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('Só pode ser criado um Texto sobre o histórico do CADir/Edite o que já existe')
        return super(TextoHistorico, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Texto do histórico do CADir"
        verbose_name = "Texto do histórico do CADir"
