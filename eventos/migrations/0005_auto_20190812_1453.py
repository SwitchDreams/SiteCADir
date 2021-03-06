# Generated by Django 2.2.3 on 2019-08-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20190725_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='more_info_img',
            field=models.ImageField(blank=True, help_text='Caso o evento tenha um pdf/foto com mais informações', upload_to='evento_more_info', verbose_name='Foto com mais informações'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='end',
            field=models.TimeField(help_text='Caso o Evento seja o dia inteiro coloque qualquer horário', verbose_name='Horário de término'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='show_img',
            field=models.ImageField(blank=True, default='CADir_logo.png', upload_to='evento_show_img', verbose_name='show_img'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='start',
            field=models.TimeField(help_text='Caso o Evento seja o dia inteiro coloque qualquer horário', verbose_name='Horário de começo'),
        ),
    ]
