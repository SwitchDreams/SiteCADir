# Generated by Django 2.2.3 on 2019-07-28 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Guia',
                'verbose_name_plural': 'Guias',
            },
        ),
    ]
