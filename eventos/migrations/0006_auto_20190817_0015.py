# Generated by Django 2.2.3 on 2019-08-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20190812_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='end',
            field=models.TimeField(blank=True, help_text='Caso o Evento seja o dia inteiro coloque qualquer horário', null=True, verbose_name='Horário de término'),
        ),
    ]