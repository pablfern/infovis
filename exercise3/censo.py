# -*- coding: utf-8 -*-

def viviendas(source='VIVIENDA.csv', destination='VIVIENDA2.csv'):
    tipvv = {'0': u' ', '1': u'Particular', '2': u'Colectiva',}
    v01 = { 
            '0': u' ',
            '1': u'Casa',
            '2': u'Rancho',
            '3': u'Casilla',
            '4': u'Departamento',
            '5': u'Pieza en inquilinato',
            '6': u'Pieza en hotel familiar o pensión',
            '7': u'Local no construido para habitación',
            '8': u'Vivienda móvil',
            '9': u'Persona/s viviendo en la calle',
          }
    v02 = {
            '0': u' ',
            '1': u'Con personas presentes',
            '2': u'Con todas las personas temporalmente ausentes',
            '3': u'En alquiler',
            '4': u'En construcción',
            '5': u'Se usa como comercio, oficina o consultorio',
            '6': u'Se usa para vacaciones, fin de semana u otro uso temporal',
            '7': u'Por otra razón' 
    }
    v00 = {
            '0': u' ',
            '1': u'Hogar de ancianos',
            '2': u'Hogar de menores',
            '3': u'Colegio internado',
            '4': u'Campamento/obrador',
            '5': u'Hospital',
            '6': u'Prisión',
            '7': u'Cuartel',
            '8': u'Hogar de religiosos',
            '9': u'Hotel turístico',
            '10': u'Otros',
    }
    urp = {
            '0': u' ',
            '1': u'Urbano',
            '2': u'Rural agrupado',
            '3': u'Rural disperso',
    }
    incalserv = {
            '0': u' ',
            '1': u'Satisfactoria',
            '2': u'Básica',
            '3': u'Insuficiente',
    }
    inmat = {
            '0': u' ',
            '1': u'Calidad I',
            '2': u'Calidad II',
            '3': u'Calidad III',
            '4': u'Calidad IV',
    }
    incalcons = {
            '0': u' ',
            '1': u'Satisfactoria',
            '2': u'Básica',
            '3': u'Insuficiente'
    }
# 0    VIVIENDA_REF_ID
# 1    RADIO_REF_ID
# 2    TIPVV
# 3    V01
# 4    V02
# 5    V00
# 6    URP
# 7    INCALSERV
# 8    INMAT
# 9    MUNI
# 10    LOCAL
# 11    INCALCONS
# 12   TOTHOG

    with open(source) as infile, open(destination, 'w') as outfile:
        header = True
        for line in infile:
            if header:
                header = False
                continue
            aux_line = line.split(';')
            aux_line[2] = replace(2, aux_line, tipvv)
            aux_line[3] = replace(3, aux_line, v01)
            aux_line[4] = replace(4, aux_line, v02)
            aux_line[5] = replace(5, aux_line, v00)
            aux_line[6] = replace(6, aux_line, urp)
            aux_line[7] = replace(7, aux_line, incalserv)
            aux_line[8] = replace(8, aux_line, inmat)
            aux_line[11] = replace(11, aux_line, incalcons)
            final = u''
            for a in aux_line:
                final += a + ';'
            final = final[:-1]
            outfile.write(final.encode('utf-8'))

def replace(index, vector, my_dict):
    return my_dict[vector[index]]


#     CREATE TABLE vivienda
# (
#   vivienda_id serial NOT NULL,
#   radio_id integer,
#   tipo_de_vivienda character varying(60),
#   tipo_de_vivienda_particular character varying(60),
#   condicion_de_ocupacion character varying(60),
#   tipo_de_vivienda_colectiva character varying(60),
#   tipo_de_area character varying(60),
#   calidad_de_conexion_de_servicios character varying(60),
#   calidad_de_materiales character varying(60),
#   municipio integer,
#   localidad integer,
#   calidad_constructiva character varying(60),
#   total_de_hogares integer,
#   roulo character varying(60),
#   CONSTRAINT vivienda_id_pkey PRIMARY KEY (vivienda_id)
# )
# WITH (
#   OIDS=FALSE
# );
# ALTER TABLE vivienda
#   OWNER TO postgres;
