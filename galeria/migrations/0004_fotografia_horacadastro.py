# Generated by Django 5.0 on 2023-12-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='horaCadastro',
            field=models.DateTimeField(auto_now=True, verbose_name='Data e Hora'),
        ),
    ]
