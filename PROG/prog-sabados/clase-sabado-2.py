'''
NOMBRE: AGUSTIN GARCIA NAVAS

1-Generar una sublista de los animes estrenados antes de 1995:
2-Generar una sublista de los animes con más de 1 temporada:
3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
5-Generar una sub listas con un diccionario que contenga 'temporada' == 1 y una lista dentro de nombres
'''

animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 9, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 9, "personaje_principal": "Shinji Ikari"}
]


import re
import json

def normalizar_nombre(dato:str):

    if type(dato) == str:
        
        dato = re.split(' ',dato)

        cadena = ""


        for palabra in dato:

            cadena += palabra.lower() + ' '


        return cadena[:-1]

def ordenar_lista(lista:list,clave:str):

    if type(lista) == list and len(lista) > 1:

        flag = True

        opcion = input('Desea ordenar la lista de forma asc o desc? ')

        while re.search('^(?!asc$|desc$)',opcion,re.IGNORECASE):

            opcion = input('ERROR Desea ordenar la lista de forma asc o desc? ')

        valor_retorno = None

        while flag == True:

            flag = False

            for i in range(len(lista)-1):

                if clave in lista[i] and clave in lista[i+1]:

                    if opcion == 'asc' and lista[i][clave] > lista[i+1][clave]:

                        auxiliar = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = auxiliar
                        flag = True

                    elif opcion == 'desc' and lista[i][clave] < lista[i+1][clave]:

                        auxiliar = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = auxiliar
                        flag = True

                else:

                    valor_retorno = 'La clave no existe'
                    break

    else:

        valor_retorno = 'Error en la lista ingresada'

    if valor_retorno != None:

        print(valor_retorno)

    else:

        return lista
    

def normalizar_cadena_lista(lista:list,clave:str):

    if type(lista) == list:

        for elemento in lista:

            elemento[clave] = normalizar_nombre(elemento[clave])

        

        return lista

nombre_normalizado = normalizar_cadena_lista(animes_90s,'personaje_principal')
ordenada = ordenar_lista(nombre_normalizado,'personaje_principal')
print(ordenada)

