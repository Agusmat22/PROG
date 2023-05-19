import re
import json

#LLAMO A LAS FUNCIONES QUE TENGO EN OTRO ARCHIVO
import funciones_genericas

""" Ejercicio tipo parcial
1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)
2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
manera ascendente ('asc') o descendente ('desc')
3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar
de manera ascendente ('asc') o descendente ('desc')
4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la
condición de superar o no el promedio (preguntar al usuario la condición:
'menor' o 'mayor') se deberá listar en consola aquellos que cumplan con ser
mayores o menores según corresponda.
5. Buscar héroes por inteligencia [good, average, high] y listar en consola los
que cumplan dicha búsqueda. (Usando RegEx)
6. Exportar a CSV la lista de héroes ordenada según opción elegida
anteriormente [1-4] """


#ABRIR JSON
def abrir_json_de_cero(nombre:str):

    with open(nombre,'r') as archivo:

        diccionario = json.load(archivo)

        return diccionario['heroes']
        

lista_personajes = abrir_json_de_cero('Clase-8\\data_stark.json')
lista_personajes_copia = lista_personajes.copy()


#1

def listar_n_heroes(lista:list):

    opcion = funciones_genericas.pedir_dato("Ingrese la cantidad de heroes que desea imprimir: ")

    while re.search('[^0-9*$]',opcion,re.IGNORECASE) or int(opcion) > len(lista):

        opcion = funciones_genericas.pedir_dato("ERROR Ingrese la cantidad de heroes que desea imprimir: ")

    opcion = int(opcion)

    lista_heroes_n = []


    for posicion in range(opcion):

        lista_heroes_n.append(lista[posicion])


    return lista_heroes_n


#contenido =listar_n_heroes(lista_personajes_copia)

#2 y #3

def ordenar_lista_por_altura(lista:list,clave:str):

    if len(lista) > 1:

        flag = True

        opcion = funciones_genericas.pedir_dato("Desea ordenar la lista de forma asc o desc? ")

        while re.search('^(?!asc$|desc$)',opcion,re.IGNORECASE):

            opcion = funciones_genericas.pedir_dato("ERROR Desea ordenar la lista de forma asc o desc? ")

        opcion = opcion.lower()
    
        while flag == True:

            flag = False

            for i in range(len(lista)-1):

                if clave in lista[i] and clave in lista[i+1]:

                    if  opcion == 'asc' and lista[i][clave] > lista[i+1][clave]:

                        auxiliar = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = auxiliar
                        flag = True
                    
                    elif  opcion == 'desc' and lista[i][clave] < lista[i+1][clave]:

                        auxiliar = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = auxiliar
                        flag = True

        
    
    return lista

""" 
lista_normalizada = funciones_genericas.normalizar_numero_lista(lista_personajes_copia,'altura')
lista_normalizada = funciones_genericas.normalizar_numero_lista(lista_personajes_copia,'fuerza')

 """

#4


def filtrar_heroes_por_promedio(lista:list,clave:str,promedio):

    if type(promedio) != int and type(promedio) != float:

        return 'Error, el promedio ingresado no es de tipo numerico'
    else:

        opcion = funciones_genericas.pedir_dato('Desea filtrar los heroes mayor o menor al promedio? ')

        while re.search('^(?!menor$|mayor$)',opcion,re.IGNORECASE):

            opcion = funciones_genericas.pedir_dato('ERROR Desea filtrar los heroes mayor o menor al promedio? ')


        valor_retorno = None
        lista_heroes_filtrados = []


        opcion = opcion.lower()

        for heroe in lista:

            if clave in heroe:

                if opcion == 'mayor' and heroe[clave] > promedio:

                    lista_heroes_filtrados.append(heroe)

                elif opcion == 'menor' and heroe[clave] < promedio:

                    lista_heroes_filtrados.append(heroe)

            else:

                valor_retorno = 'La clave no existe en el diccionario'
                break

        
        if valor_retorno != None:

            print(valor_retorno)

        else:

            valor_retorno = lista_heroes_filtrados

            return valor_retorno


""" promedio_calculado = funciones_genericas.calcular_promedio(lista_personajes_copia,'altura')
contenido = filtrar_heroes_por_promedio(lista_normalizada,'altura',promedio_calculado) """


#5

def obtener_heroes_por_inteligencia(lista:list,clave:str):

    lista_heroes_inteligencia = []

    lista_inteligencias = ['good', 'average', 'high']

    valor_retorno = None

    for inteligencia in lista_inteligencias:

        for heroe in lista:

            if clave in heroe:

                if inteligencia == heroe[clave]:

                    lista_heroes_inteligencia.append(heroe)
            
            else:

                valor_retorno = 'La clave no existe en el diccionario'
                break
    

    if valor_retorno != None:

        print(valor_retorno)

    else:

        return lista_heroes_inteligencia




def crear_archivo_csv(nombre:str,lista:list):

    if type(lista) == list:

        with open(nombre,'w') as archivo:

            for elemento in lista:

                mensaje = elemento['nombre'] +','+ str(elemento['altura']) + ',' +  str(elemento['peso']) + ',' + str(elemento['fuerza']) + '\n'

                archivo.write(mensaje)

        mensaje = 'Se creo el archivo correctamente'

    else:

        mensaje = 'Error al crear el archivo'

    print(mensaje)





def app_stark(lista:list,clave:str):

    lista_validar = funciones_genericas.validar_lista(lista)

    if lista_validar == True:

        lista = funciones_genericas.normalizar_texto_lista(lista_personajes_copia,'inteligencia')
        lista = funciones_genericas.normalizar_numero_lista(lista_personajes_copia,'altura')
        lista = funciones_genericas.normalizar_numero_lista(lista_personajes_copia,'fuerza')

        flag = True

        while flag == True:

            funciones_genericas.imprimir_menu_opciones('*** DEBE SELECCIONAR UNA OPCION ***\n'
                                                        '\n'
                                                        '1 - Listar la cantidad de superheroes que deseada\n'
                                                        '2 - Listar heroes por su altura\n'
                                                        '3 - Listar heroes por su fuerza\n'
                                                        '4 - Listar heroes por mayor o menor a su promedio\n'
                                                        '5 - Salir\n')

            opcion = funciones_genericas.pedir_dato('Ingrese un numero del [1-5]: ')

            while re.search('^(?!1$|2$|3$|4$|5$)',opcion,re.IGNORECASE):

                opcion = funciones_genericas.pedir_dato('ERROR Ingrese un numero del [1-5]: ')


            if opcion == '1':

                contenido =listar_n_heroes(lista)
                funciones_genericas.imprimir_lista(contenido)
                nombre_archivo = 'listado_n_heroes.csv'

            elif opcion == '2':

                contenido = ordenar_lista_por_altura(lista,'altura')
                funciones_genericas.imprimir_lista(contenido,'altura')
                nombre_archivo = 'lista_ordenada_por_altura.csv'

            elif opcion == '3':

                contenido = ordenar_lista_por_altura(lista,'fuerza')
                funciones_genericas.imprimir_lista(contenido,'fuerza')
                nombre_archivo = 'lista_ordenada_por_fuerza.csv'


            elif opcion == '4':

                promedio_calculado = funciones_genericas.calcular_promedio(lista,clave)
                contenido = filtrar_heroes_por_promedio(lista,clave,promedio_calculado)
                nombre_archivo = 'lista_filtrada_por_promedio.csv'

            elif opcion == '5':

                break


            
            #crear_archivo_csv(nombre_archivo,contenido)
            
    else:

        print('Error en la lista ingresada')

            
            

#app_stark(lista_personajes_copia,'altura')

lista_normalizada = funciones_genericas.normalizar_texto_lista(lista_personajes_copia,'color_ojos')
lista = funciones_genericas.obtener_keys_repetidas(lista_normalizada,'color_ojos')
print(lista)





        




        
