from django.shortcuts import render
from django.http import JsonResponse
from models import Vivienda
from django.db.models import Count


# Retorna un JSON con la cantidad de viviendas en cada municipio.
# Acepta un parametro opcional "limit" para obtener los N primeros elementos.
def viviendas_por_municipio(request):
    viviendas = Vivienda.objects\
                        .values('municipio')\
                        .annotate(total=Count('municipio'))\
                        .order_by('-total')
    limit = request.GET.get('limit')
    if limit:
        viviendas = viviendas[:limit]
    data = { 'key': 'Cantidad de viviendas por municipio',
              'values': None, }
    values = []
    order = 1
    for element in viviendas:
        values.append({"orden": order,
                       "municipio": element['municipio'],
                       "nombre": '',
                       "cant_viviendas": element['total'],
                       })
        order += 1
    data['values'] = values
    return JsonResponse(data)


# Retorna un JSON con la cantidad de viviendas en cada municipio
# agrupadas por el tipo de vivienda.
# Acepta un parametro opcional "limit" para obtener los N primeros elementos.
def viviendas_agrupadas_por_tipo(request):
    limit = request.GET.get('limit')
    viviendas_id = map(lambda x: x['municipio'], Vivienda.objects\
                                                         .values('municipio')\
                                                         .annotate(total=Count('municipio'))\
                                                         .order_by('-total')[:limit])
    vivienda = Vivienda.objects\
                       .filter(municipio__in=viviendas_id)\
                       .values('municipio', 'tipo_de_vivienda_particular')\
                       .annotate(Count('municipio'),Count('tipo_de_vivienda_particular'))
    tipo_de_vivienda = Vivienda.objects.values('tipo_de_vivienda_particular').annotate(Count('tipo_de_vivienda_particular'))
    
    mymap = {}
    for tipo in tipo_de_vivienda:
        mymap[tipo['tipo_de_vivienda_particular']] = []
    data = []
    
    for v in vivienda:
        mymap[v['tipo_de_vivienda_particular']].append({'cantidad': v['municipio__count'],
                                                        'municipio': v['municipio'],})
    for key, val in mymap.iteritems():
        data.append({'key': key,
                     'values': val,})
    return JsonResponse(data, safe=False)