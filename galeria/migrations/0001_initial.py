# Generated by Django 5.0 on 2023-12-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('legenda', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=250)),
            ],
        ),
    ]
