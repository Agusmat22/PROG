import json
import re


def abrir_csv(nombre:str):

    with open(nombre,'r') as archivo:

        lista_elementos = []

        for elemento in archivo:
            
            diccionario = {}

            linea = re.split(',',elemento)


            diccionario['nombre'] = linea[0]
            diccionario['edad'] = linea[1]
            diccionario['apellido'] = linea[2]
            diccionario['altura'] = re.sub('\n','',linea[3])

            lista_elementos.append(diccionario)

        return lista_elementos
    

lista = abrir_csv('prog-sabados\\lista_personajes.csv')
lista_copia = lista.copy()



def ordenamientos(lista:list,clave:str):

    if len(lista) <= 1:

        opcion = input('Desea calcular de modo asc o desc? ')

        while re.search('^(?!asc$|desc$)',opcion,re.IGNORECASE):

            opcion = input('ERROR Desea calcular de modo asc o desc? ')

        flag = True
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

                    valor_retorno = 'No existe la clave en el diccionario'
    
    else: 

        return lista


    if type(valor_retorno) == str:

        print(valor_retorno)

    else:

        return lista