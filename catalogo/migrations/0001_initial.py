# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('director', models.CharField(max_length=50)),
                ('escritor', models.CharField(max_length=50)),
                ('estudio', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('duracion', models.IntegerField()),
                ('clasificacion', models.CharField(max_length=15)),
            ],
        ),
    ]
