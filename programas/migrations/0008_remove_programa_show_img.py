# Generated by Django 2.2.3 on 2019-07-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0007_auto_20190717_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='show_img',
        ),
    ]
