# Generated by Django 2.2.3 on 2019-08-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0004_textohistorico'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestacaoDeContas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome que aparecerá no site(Institucional)', max_length=60, verbose_name='Nome')),
                ('file', models.FileField(upload_to='prestacao_de_contas_pdf', verbose_name='Arquivo')),
            ],
            options={
                'verbose_name': 'Prestação de conta',
                'verbose_name_plural': 'Prestações de Conta',
            },
        ),
    ]