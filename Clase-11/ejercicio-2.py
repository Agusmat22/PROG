import re

""" 1.      Obtener una lista con los nombres de
todas las series de anime.


2.      Obtener las series de anime lanzadas
después de 1995.


3.      Obtener la suma de los años de
lanzamiento de las series.


4.      Realizar una copia superficial de la
lista de series.


5.      Realizar una copia profunda de la
lista de series.


6.      Obtener el año de lanzamiento de una
serie utilizando una función de diccionario.


7.      Obtener una lista de tuplas con los
pares clave-valor de una serie utilizando una función de diccionario.


8.      Eliminar una serie de la lista por su
índice utilizando una función de lista.


9.      Obtener una lista con los nombres de
las series en mayúsculas utilizando una función de transformación.


10.   Obtener las series de anime con
nombres que contengan la palabra "Adventure" utilizando una función
de filtrado.


11.   Generar una función que busque los
nombres de las series con el rating mayor a 8.5
 """


series = [

    {"nombre": "Dragon Ball Z", "año": 1989},
    {"nombre": "Sailor Moon", "año": 1992},
    {"nombre": "Pokemon", "año": 1997},
    {"nombre": "Digimon Adventure","año": 1999},
    {"nombre": "Yu Yu Hakusho", "año": 1992},
    {"nombre": "Neon Genesis Evangelion", "año": 1995},
    {"nombre": "One Piece", "año": 1999},
    {"nombre": "Rurouni Kenshin Adventure", "año": 1996}

]

#1. Obtener una lista con los nombres de todas las series de anime.

def obtener_nombres(diccionario:list):

    nombre = diccionario.get('nombre')

    return nombre

""" valor = list(map(obtener_nombres,series))
print(valor) """

#2. Obtener las series de anime lanzadas después de 1995.
""" 
lista = list(filter(lambda elem : elem['año'] > 1995,series))
print(lista) """

#3.  Obtener la suma de los años de lanzamiento de las series.

""" from functools import reduce

suma = reduce(lambda a, b: a + b,map(lambda serie: serie['año'],series))
print(suma) """

#4. Realizar una copia superficial de la lista de series.

""" lista_copia_superficial = series.copy()
 """
#5. Realizar una copia profunda de la lista de series.

from copy import deepcopy

""" lista_copia_profunda = deepcopy(series)
print(lista_copia_profunda) """


#6. Obtener el año de lanzamiento de una serie utilizando una función de diccionario.

""" contenido_serie = series[1].get('año','no existe')
print(contenido_serie) """

#7.      Obtener una lista de tuplas con los pares clave-valor de una serie utilizando una función de diccionario.

""" lista_tuplas = list(map(lambda serie: list(serie.items()),series))
print(lista_tuplas) """

#8. Eliminar una serie de la lista por su índice utilizando una función de lista.

""" elemento_eliminado = series.pop(2)
print(elemento_eliminado)
print(series) """

#9. Obtener una lista con los nombres de las series en mayúsculas utilizando una función de transformación.

""" lista_nombres = list(map(lambda elem: elem.get('nombre').upper(),series))
print(lista_nombres) """

#10. Obtener las series de anime con nombres que contengan la palabra "Adventure" utilizando una función de filtrado.

""" lista_series_adventura = list(filter(lambda elem: 'Adventure' in elem['nombre'],series))
print(lista_series_adventura) """