# Generated by Django 2.2.3 on 2019-08-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0010_programa_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='audio',
            field=models.FileField(blank=True, upload_to='media/audio_programas'),
        ),
    ]