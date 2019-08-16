from django.db import models


# Create your models here.

class Fotos(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome só para lembrar qual foto é')
    foto = models.ImageField('Foto', upload_to='fotos_principal')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Fotos"
        verbose_name = "Foto"

    def delete(self, *args, **kwargs):
        print(self.nome)
        if self.nome == "1 Slider" or self.nome == "2 Slider" or self.nome == "3 Slider" \
                or self.nome == "1 Foto Divisão" or self.nome == "2 Foto Divisão":
            return
        else:
            super(Fotos, self).delete(*args, **kwargs)