#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS
#FECHA: 10/5/2023 

""" 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.
2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
ingresada por el usuario por pantalla.
3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de
manera ascendente ('asc') o descendente ('desc').
4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
dicha búsqueda. (Usando RegEx).
5) Exportar a CSV la lista de juegos según opción 1 o 3.
6) Salir. """



import re
import json

#IMPORTO FUNCIONES

import funciones_genericas

def abrir_json(nombre:str):

    with open(nombre,'r') as archivo:

        diccionario = {}

        diccionario = json.load(archivo)

        return diccionario['juegos']


lista_juegos = abrir_json('Parcial-1\\data_pp.json')
lista_juegos_copia = lista_juegos.copy()

# 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.

def obtener_juegos_por_genero_diferente(lista:list,clave:str):

    lista_juegos_genero_distinto = []
    valor_retorno = None

    for juego in lista:

        if clave in juego:

            if re.search('^(?!pelea)',juego[clave],re.IGNORECASE):

                lista_juegos_genero_distinto.append(juego)
        

        else:

            valor_retorno = 'La clave no existe dentro del diccionario'
            break

    if valor_retorno != None:

        print(valor_retorno)

    else:

        return lista_juegos_genero_distinto



#2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
#ingresada por el usuario por pantalla.

def obtener_juegos_por_decada(lista:list,clave:str):

    opcion = funciones_genericas.pedir_dato("Ingrese la decada que desea: ")

    validacion_opcion = funciones_genericas.validar_numero(opcion)

    while validacion_opcion == False:

        opcion = funciones_genericas.pedir_dato("ERRRO Ingrese la decada que desea: ")
        validacion_opcion = funciones_genericas.validar_numero(opcion)

    opcion = int(opcion)


    lista_juegos_decada = []

    valor_retorno = None

    for juego in lista:

        if clave in juego :

            if juego[clave] >= opcion and juego[clave] <= opcion + 9:

                lista_juegos_decada.append(juego)

        else: 
            
            valor_retorno = 'La clave no existe dentro del diccionario'

    
    if valor_retorno != None:

        print(valor_retorno)

    else:

        return lista_juegos_decada




#4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
# dicha búsqueda. (Usando RegEx).

def obtener_juegos_modo(lista:list,clave:str):

    lista_juegos_por_modos = []

    valor_retorno = None

    for juego in lista:

        if clave in juego:

            if re.search('multijugador|cooperativo',juego[clave],re.IGNORECASE):

                lista_juegos_por_modos.append(juego)

        else:

            valor_retorno = 'La clave no existe en el diccionario'

    
    if valor_retorno != None:

        print(valor_retorno)
    else:

        return lista_juegos_por_modos





def app_juegos(lista:list):

    lista_validar = funciones_genericas.validar_lista(lista)

    if lista_validar == True:

        lista = funciones_genericas.normalizar_texto_lista(lista,'genero')
        lista = funciones_genericas.normalizar_numero_lista(lista,'anio')
        lista = funciones_genericas.normalizar_texto_lista(lista,'empresa')

        flag = True

        while flag == True:

            funciones_genericas.imprimir_menu_opciones('*** DEBE SELECCIONAR UNA OPCION ***\n'
                                                        '\n'
                                                        '1 - Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”\n'
                                                        '2 - Mostrar la cantidad de juegos de una década determinada\n'
                                                        '3 - Listar los juegos ordenados por Empresa.\n'
                                                        '4 - Listar juegos por modo [cooperativo y multijugador]\n'
                                                        '5 - Salir\n')

            opcion = funciones_genericas.pedir_dato('Ingrese un numero del [1-5]: ')

            while re.search('^(?!1$|2$|3$|4$|5$)',opcion,re.IGNORECASE):

                opcion = funciones_genericas.pedir_dato('ERROR Ingrese un numero del [1-5]: ')


            if opcion == '1':

                contenido = obtener_juegos_por_genero_diferente(lista,'genero')
                funciones_genericas.imprimir_lista(contenido)
                nombre_archivo = 'juegos_por_genero_diferente.csv'

            elif opcion == '2':

                contenido = obtener_juegos_por_decada(lista,'anio')
                funciones_genericas.imprimir_lista(contenido)
                nombre_archivo = 'juegos_por_decada.csv'
                

            elif opcion == '3':

                contenido = funciones_genericas.ordenar_lista_keys(lista,'empresa')
                funciones_genericas.imprimir_lista(contenido)
                nombre_archivo = 'ordenar_lista_empresa.csv'


            elif opcion == '4':

                contenido = obtener_juegos_modo(lista,'modo')
                funciones_genericas.imprimir_lista(contenido)
                nombre_archivo = 'juegos_por_modo.csv'
                

            elif opcion == '5':

                break 


            
            if opcion == '1' or opcion == '3':

                funciones_genericas.crear_archivo_csv(nombre_archivo,contenido)
            
    else:

        print('Error en la lista ingresada')


app_juegos(lista_juegos_copia)