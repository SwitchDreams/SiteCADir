# Generated by Django 2.1.1 on 2019-07-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0005_programa_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='tipo',
            field=models.CharField(choices=[('ATL', 'Atlética'), ('EJ', 'Empresa Junior'), ('GE', 'Grupos de extensão'), ('OUT', 'Outros')], default='OUT', max_length=3, verbose_name='tipo'),
        ),
    ]
