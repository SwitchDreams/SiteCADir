# Generated by Django 2.2.3 on 2019-08-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0011_auto_20190802_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='audio',
        ),
    ]