import re

lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

#copia
from copy import deepcopy

lista_copia = deepcopy(lista_diccionario)

def calcular_iva(diccionario:dict):

    iva_calculado = diccionario['precio']['sin_iva'] + diccionario['precio']['sin_iva'] * 21 / 100

    diccionario['precio']['con_iva'] = iva_calculado

    return diccionario


lista_copia = list(map(calcular_iva,lista_copia))

mensaje = 'Nombre | Precio sin iva | Precio con iva\n'

for elemento in lista_copia:


    mensaje += elemento['nombre']+' | '+str(elemento['precio']['sin_iva']) +' | '+str(elemento['precio']['con_iva']) + '\n'



#VALIDO SI HAY ALGUN ELEMENTO MAYOR A 6000
lista_filtrada = list(filter(lambda elemento: elemento['precio']['con_iva'] > 1000,lista_copia))


#AGREGO UN DICCIONARIO A LA LISTA
lista_copia.insert(-1,{'nombre' : 'Rastrillo','precio': {'sin_iva': 4450.00,'con_iva':0.00}})













