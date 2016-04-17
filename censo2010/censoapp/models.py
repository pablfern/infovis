# -*- coding: utf-8 -*-
from django.db import models


class Vivienda(models.Model):
    radio_id = models.PositiveIntegerField(verbose_name=u'radio id')
    tipo_de_vivienda = models.CharField(max_length=60, verbose_name=u'tipo de vivienda')
    tipo_de_vivienda_particular = models.CharField(max_length=60, verbose_name=u'tipo de vivienda particular')
    condicion_de_ocupacion = models.CharField(max_length=60, verbose_name=u'condición de ocupación')
    tipo_de_vivienda_colectiva = models.CharField(max_length=60, verbose_name=u'tipo de vivienda colectiva')
    tipo_de_area = models.CharField(max_length=60, verbose_name=u'tipo de area')
    calidad_de_conexion_de_servicios = models.CharField(max_length=60, verbose_name=u'calidad de conexión de servicios')
    calidad_de_materiales = models.CharField(max_length=60, verbose_name=u'calidad de materiales')
    municipio = models.PositiveIntegerField(verbose_name=u'municipio')
    localidad = models.PositiveIntegerField(verbose_name=u'localidad')
    calidad_constructiva = models.CharField(max_length=60, verbose_name=u'calidad constructiva')
    total_de_hogares = models.PositiveIntegerField(verbose_name=u'total de hogares')