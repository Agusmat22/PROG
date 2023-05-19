""" Se tiene la siguiente lista de diccionarios:
lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

1)Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:
2)De debra mapear al precio con iva, sumando el 21% sobre el precio sin iva, Mostrar los datos por pantalla.
4)Modificar el nombre de Destornillador por Destornillador Philips. Mostrar los datos por pantalla.
6)Agregar una herramienta con sus respectivos datos.
7)Mostrar los datos.
8)Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas. Mostrar los datos.
9)Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas. """

lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

#COPIA PROFUNDA

import re

#1)
from copy import deepcopy

lista_copia = deepcopy(lista_diccionario)

#2
def agregar_iva(diccionario:dict):

    iva_calculado = diccionario['precio']['sin_iva'] + diccionario['precio']['sin_iva'] * 21 / 100

    diccionario['precio']['con_iva'] = iva_calculado 

    return diccionario

lista_copia = list(map(agregar_iva,lista_copia))
print(lista_copia)







#4)CAMBIAR NOMBRE HERRAMIENTA

for i,elemento in enumerate(lista_copia):

    if re.search('^destornillador$',elemento['nombre'],re.IGNORECASE):

        lista_copia[i].update({'nombre':'Philips'})

#6)AGREGAR UNA HERRAMIENTA
lista_copia.append({'nombre':'Llave Cruz','precio': {'sin_iva': 1850.00,'con_iva':0.00}})


#8)ELIMINAR DOS HERRAMIENTAS

herramientas_eliminadas = []

for elemento in range(2):

    herramientas_eliminadas.append(lista_copia.pop(-2))


print(lista_copia)
   

        
