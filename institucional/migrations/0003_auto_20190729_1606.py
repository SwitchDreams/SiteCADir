# Generated by Django 2.2.3 on 2019-07-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0002_auto_20190729_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='nome',
            field=models.CharField(max_length=60, unique=True, verbose_name='Nome'),
        ),
    ]