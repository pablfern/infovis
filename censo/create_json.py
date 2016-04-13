# -*- coding: utf-8 -*-


def chart2():
	house_types = [u'No Sabe No contesta',u'Casa',u'Casilla',u'Departamento',u'Local no construido para habitación',u'Persona/s viviendo en la calle',u'Pieza en hotel familiar o pensión',u'Pieza en inquilinato',u'Rancho',u'Vivienda móvil']
	data = [[u'Cordoba',454,332555,1424,134162,405,154,609,1297,1937,28],[u'La Matanza',149,359347,14658,64903,848,65,149,2891,4464,46],[u'Rosario',421,219272,4323,129210,344,69,588,533,2763,24],[u'General Pueyrredon',573,180328,3008,121982,404,45,59,378,1191,54],[u'La Plata',377,171940,12007,72567,295,33,308,315,1878,42],[u'Lomas de Zamora',108,159427,3321,22603,230,30,42,1087,1466,10],[u'Quilmes',97,153769,5618,20547,246,27,102,669,1252,13],[u'Lanus',84,124151,1288,31352,167,20,60,425,419,5],[u'San Miguel de Tucumán',173,113766,4054,37695,133,29,138,504,1056,5],[u'Almirante Brown',78,132653,6116,15537,213,14,17,350,1287,31]]
	ans = []
	i = 0
	for house in house_types:
		values = []
		for muni in data:
			values.append({"municipio": muni[0], "cantidad": muni[i+1]})
		ans.append({"key": house, "values":values})
		i += 1
	print ans
