# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radio_id', models.PositiveIntegerField(verbose_name='radio id')),
                ('tipo_de_vivienda', models.CharField(max_length=60, verbose_name='tipo de vivienda')),
                ('tipo_de_vivienda_particular', models.CharField(max_length=60, verbose_name='tipo de vivienda particular')),
                ('condicion_de_ocupacion', models.CharField(max_length=60, verbose_name='condici\xf3n de ocupaci\xf3n')),
                ('tipo_de_vivienda_colectiva', models.CharField(max_length=60, verbose_name='tipo de vivienda colectiva')),
                ('tipo_de_area', models.CharField(max_length=60, verbose_name='tipo de area')),
                ('calidad_de_conexion_de_servicios', models.CharField(max_length=60, verbose_name='calidad de conexi\xf3n de servicios')),
                ('calidad_de_materiales', models.CharField(max_length=60, verbose_name='calidad de materiales')),
                ('municipio', models.PositiveIntegerField(verbose_name='municipio')),
                ('localidad', models.PositiveIntegerField(verbose_name='localidad')),
                ('calidad_constructiva', models.CharField(max_length=60, verbose_name='calidad constructiva')),
                ('total_de_hogares', models.PositiveIntegerField(verbose_name='total de hogares')),
            ],
        ),
    ]
