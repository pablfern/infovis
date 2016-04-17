from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns(
    '',
    url(r'^viviendas-por-municipio/$', 'censoapp.views.viviendas_por_municipio', name="viviendas-por-municipio"),
    url(r'^viviendas-agrupadas-por-tipo/$', 'censoapp.views.viviendas_agrupadas_por_tipo', name="viviendas-agrupadas-por-tipo"),
)
