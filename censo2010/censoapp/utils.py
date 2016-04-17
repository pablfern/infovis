from models import *


def vivienda_csv_to_db(file_path='/tmp/database.csv'):
    with open(file_path) as source_file:
        lines = source_file.readlines()
        for line in lines:
            splited = line.split('|')
            Vivienda.objects.create(
                radio_id=int(splited[1]),
                tipo_de_vivienda=splited[2],
                tipo_de_vivienda_particular=splited[3],
                condicion_de_ocupacion=splited[4],
                tipo_de_vivienda_colectiva=splited[5],
                tipo_de_area=splited[6],
                calidad_de_conexion_de_servicios=splited[7],
                calidad_de_materiales=splited[8],
                municipio=int(splited[9]),
                localidad=int(splited[10]),
                calidad_constructiva=splited[11],
                total_de_hogares=int(splited[12])
                )



