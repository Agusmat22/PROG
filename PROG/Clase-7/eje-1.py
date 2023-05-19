#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS

from data_stark import lista_personajes

import re

#llamo a la funcion del ejerciocio #02
from funciones_02 import imprimir_dato

from funciones_02 import stark_normalizar_datos

from funciones_02 import dividir

from funciones_02 import calcular_promedio



#llamo a todas las funciones del ejercicio #01

import funciones_01


#IMPORTAR LISTAS A UN JSON, SI EXISTE ALGO EN ESE JSON LO SOBREESCRIBE
def importar_listas(lista_generica:list,nombre:str):

    archivo = open(nombre,'w+')

    archivo.write(json.dumps(lista_generica))

    archivo.close()


#importar_listas(lista_personajes,'C:/Users/Lisandro/Desktop/PROG/Clase-7/datos.json')







""" 1.1. Crear la función "imprimir_menu_desafio_5" que imprima el menú de
opciones por pantalla (las opciones son las que se van a utilizar para
acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
Reutilizar la función 'imprimir_dato' realizada en una práctica anterior. """

#reutiliza la funcion que se encuentr en el desafio #02, e imprime el menu
def imprimir_menu_desafio_5():

    imprimir_dato('A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M \n'
                    'B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n'
                    'C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n'
                    'D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n'
                    'E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n'
                    'F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n'
                    'G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n'
                    'H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n'
                    'I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n'
                    'J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n'
                    'K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n'
                    'L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene").\n'
                    'M. Listar todos los superhéroes agrupados por color de ojos.\n'
                    'N. Listar todos los superhéroes agrupados por color de pelo.\n'
                    'O. Listar todos los superhéroes agrupados por tipo de inteligencia\n'
                    'Z. Salir\n'
    )

""" 1.2. Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
de imprimir el menú de opciones y le pedirá al usuario que ingrese la
letra de una de las opciones elegidas, deberá validar la letra usando
RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
retornará -1. El usuario puede ingresar tanto letras minúsculas como
mayúsculas y ambas se deben tomar como válidas
Reutilizar la función 'imprimir_menu_Desafio_5' """

#imprimo el menu y toma un dato por input y retorna el dato si es valido y sino -1
def stark_menu_principal():

    imprimir_menu_desafio_5()

    opcion = input("Ingrese una opcion: ")

    #pregunto SEA de la A-O y la Z
    if re.search('^[a-oz]$',opcion,re.IGNORECASE):

        valor_retorno = opcion
    
    else:

        valor_retorno = -1
        
    return valor_retorno

""" 1.3. Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
lista de héroes y se encargará de la ejecución principal de nuestro
programa. (usar if/elif o match según prefiera) Reutilizar las funciones
con prefijo 'stark_' donde crea correspondiente. """

def stark_marvel_app_5(lista_heroes:list):

    while True:

        opcion = stark_menu_principal()

        while opcion == -1:

            opcion = stark_menu_principal()

        opcion = opcion.lower()

        if re.search('a',opcion):

            valor_retorno = funciones_01.obtener_superheroes_masculino(lista_heroes)
        
        elif re.search('b',opcion):

            valor_retorno = funciones_01.obtener_superheroes_femenino(lista_heroes)

        elif re.search('c',opcion):

            valor_retorno = funciones_01.obtener_superheroe_mas_alto_masculino(lista_heroes)

        elif re.search('d',opcion):

            valor_retorno = funciones_01.obtener_superheroe_mas_alto_femenino(lista_heroes)
        
        elif re.search('e',opcion):

            valor_retorno = funciones_01.obtener_superheroe_mas_bajo_masculino(lista_heroes)
        
        elif re.search('f',opcion):

            valor_retorno = funciones_01.obtener_superheroe_mas_bajo_femenino
        
        elif re.search('g',opcion):

            valor_retorno = funciones_01.obtener_altura_promedio_superheroes_masculino(lista_heroes)

        elif re.search('h',opcion):

            valor_retorno = funciones_01.obtener_altura_promedio_superheroes_femenino(lista_heroes)

        elif re.search('i',opcion):

            valor_retorno = funciones_01.obtener_nombre_altura_maxima_minima(lista_heroes)

        elif re.search('j',opcion):

            valor_retorno = funciones_01.obtener_cantidad_color_ojos_superheroe(lista_heroes)

        elif re.search('k',opcion):

            valor_retorno = funciones_01.obtiene_cantidad_color_pelo_superheroe(lista_heroes)

        elif re.search('l',opcion):

            valor_retorno = funciones_01.obtiene_cantidad_inteligencias_superheroes(lista_heroes)

        elif re.search('m',opcion):

            valor_retorno = funciones_01.obtener_superheroe_color_ojos(lista_heroes)

        elif re.search('n',opcion):

            valor_retorno = funciones_01.obtener_superheroe_color_pelo(lista_heroes)

        elif re.search('o',opcion):

            valor_retorno = funciones_01.obtener_superheroe_inteligencia(lista_heroes)
        
        elif re.search('z',opcion):

            break
        


        print(valor_retorno)



""" 1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornará la lista de héroes como una lista de diccionarios. """

#IMPORTO LA BIBLIOTECA JSON
import json

#LEE EL ARCHIVO JSON Y LO RETORNA
def leer_archivo(archivo:str) ->list:

    dict_nuevo = {}

    archivo_guardado = open(archivo, 'r')

    dict_nuevo = json.load(archivo_guardado)

    archivo_guardado.close()

    return dict_nuevo['heroes']

#PRUEBA
#valor = leer_archivo('data_stark.json')

#print(valor)


""" 1.5. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
string que indicará el nombre con el cual se guardará el archivo junto
con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
tendrá un string el cual será el contenido a guardar en dicho archivo.
Debe abrirse el archivo en modo escritura+, ya que en caso de no
existir, lo creara y en caso de existir, lo va a sobreescribir La función
debera retornar True si no hubo errores, caso contrario False, además
en caso de éxito, deberá imprimir un mensaje respetando el formato:
.Se creó el archivo: nombre_archivo.csv
En caso de retornar False, el mensaje deberá decir: "Error al crear el
archivo: nombre_archivo" 
Donde nombre_archivo será el nombre que recibirá el archivo a ser
creado, conjuntamente con su extensión."""

#IMPORTO LA BIBLIOTECA PARA VALIDAR EL TIPO DE ARCHIVO SI ES FILE
import io

#CREA UN ARCHIVO CON EL NOMBRE QUE LE PASEMOS Y EL CONTENIDO INGRESADO, RETORNA TRUE EN CASO DE EXITO Y FALSE LO CONTRARIO
def guardar_archivo(nombre:str,contenido:str):
    
    
    with open(f'Clase-7\\{nombre}','w') as archivo:

        archivo.write(contenido)
    

    #VALIDO SI EL ARCHIVO ES DE TIPO FILE
    if isinstance(archivo, io.TextIOWrapper):

        valor_retornado = True

        print(f"Se creo el archivo: {nombre}")

    else:

        print(f"Error al crear el archivo: {nombre}")

        valor_retornado = False

    return valor_retornado



""" 1.6. Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula). """

#CONVIERTE LA PRIMERA LETRA DE UNA PALABRA o VARIAS EN Mayuscula y el resto en minuscula
def capitalizar_palabras(palabra:str)->str:

    if re.search('^[a-z\(\)/\s-]+$',palabra,re.IGNORECASE):

        palabra = palabra.strip()

        palabra = re.sub('-'," ",palabra)

        palabra_separada = re.split(" ",palabra)
        
        palabra_retornada = ""

        for elemento in palabra_separada:

            palabra_retornada += elemento.capitalize() + " "

        return palabra_retornada



""" 1.7. Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras' """

#RETORNA EL NOMBRE CON MAYUSCULAS EN LAS INICIALES Y EL RESTO MINUSCULAS DE UN DICCIONARIO
def obtener_nombre_capitalizado(heroe:dict):

    if type(heroe) == dict:
        
        

        nombre = capitalizar_palabras(heroe['nombre'])
        
        print(nombre)

    else:

        nombre = 'no ingreso'
    
    return nombre



""" 1.8. Crear la función 'obtener_nombre_y_dato' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y una key
(string) la cual representará la key del héroe a imprimir. La función
devolverá un string el cual contenga el nombre y dato (key) del héroe a
imprimir.
El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
El string resultante debe estar formateado al estilo: (suponiendo que la
key es fuerza)
Nombre: Venom | Fuerza: 500
Reutilizar 'obtener_nombre_capitalizado' """

#RETORNA EL NOMBRE Y EL VALOR DE LA KEY QUE QUIERA 
def obtener_nombre_y_dato(heroe:dict,key:str):

    if type(heroe) == dict and key in heroe:

        nombre = obtener_nombre_capitalizado(heroe)

        key_capitalizada = capitalizar_palabras(key)

        nombre_y_dato = f'Nombre: {nombre} | {key_capitalizada}: {heroe[key]}'

        return nombre_y_dato

""" 2.1. Crear la función 'es_genero' la cual recibirá por parámetro un
diccionario que representará un héroe y un string el cual será usado
para evaluar si el héroe coincide con el género buscado (El string
puede ser M, F o NB). retornará True en caso de que cumpla, False
caso contrario. """

#PIDE UN DICT Y UN GENERO, LA FUNCION VALIDA SI EL GENERO INGRESADO ES IGUAL AL DEL DICCIONARIO Y RETORNA TRUE LO CONTRARIO FALSE
def es_genero(heroe:dict,genero:str):

    if heroe['genero'] == genero.upper() and re.search('^m|f|nb$',genero):

        valor_retornado = True
    
    else:

        valor_retornado = False

    return valor_retornado
    

""" 2.2. Crear la función 'stark_guardar_heroe_genero' la cual recibira por
parámetro la lista de héroes y un string el cual representará el género
a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o
heroínas que coincidan con el género pasado por parámetro y
además, deberá guardar dichos nombres en un archivo con extensión
csv (cada nombre deberá ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta función el
nombre de archivo a guardar deberá respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
La función retornará True si pudo guardar el archivo, False caso
contrario. """

def stark_guardar_heroe_genero(lista_heroes:list,genero:str):

    if type(lista_heroes) == list:

        lista_heroes_coincidencia = []

        for elemento in lista_heroes:

            valor_genero = es_genero(elemento,genero)

            if valor_genero == True:

                nombre_capitalizado = obtener_nombre_capitalizado(elemento)

                lista_heroes_coincidencia.append(nombre_capitalizado)


        nombres_concatenados = ""

        for nombre in lista_heroes_coincidencia:

            nombres_concatenados += f'{nombre},'

        guardar_archivo('Clase-7\data.csv',nombres_concatenados)

    

        
        print(nombres_concatenados)

""" 3.1. Basandote en la función 'calcular_min', crear la función
'calcular_min_genero' la cual recibirá como parámetro extra un string
que representa el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el mínimo (peso, altura u otro dato) """

#CALCULA EL MINIMO DE CUALQUIER KEY NUMERICA Y RETORNA EL NOMBRE, REUTILIZA FUNCIONES DEL EJERCICIO 02
def calcular_min_genero(lista_heroes:list,key:str,genero:str):

    if type(lista_heroes) == list:

        stark_normalizar_datos(lista_heroes)

        flag = True

        valor_min = None

        nombre_heroe_min = None

        genero = genero.upper()

        for elemento in lista_heroes:


            if flag == True and elemento['genero'] == genero:

                valor_min = elemento[key]

                nombre_heroe_min = elemento['nombre']

                flag = False
                
            elif flag == False and valor_min > elemento[key] and elemento['genero'] == genero:

                valor_min = elemento[key]
                
                nombre_heroe_min= elemento['nombre']

        
        return nombre_heroe_min
    

""" 3.2. Basandote en la función 'calcular_max', crear la función
'calcular_max_genero' la cual recibirá como parámetro extra un string
que representará el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el máximo (peso, altura u otro dato) """

#CALCULA EL MAXIMO DE CUALQUIER KEY NUMERICA Y RETORNA EL NOMBRE, REUTILIZA FUNCIONES DEL EJERCICIO 02
def calcular_max_genero(lista_heroes:list, key:str, genero:str):

    if type(lista_heroes) == list:

        stark_normalizar_datos(lista_heroes)

        flag = True

        valor_max = None
        
        nombre_valor_max = None

        genero = genero.upper()

        for elemento in lista_heroes:

            if key in elemento:

                if flag == True and elemento['genero'] == genero:

                    valor_max = elemento[key]

                    nombre_valor_max = elemento['nombre']

                    flag = False

                elif flag == False and elemento[key] > valor_max and elemento['genero'] == genero:

                    valor_max = elemento[key]

                    nombre_valor_max = elemento['nombre']


        return nombre_valor_max


""" 3.3 Basandote en la funcion 'calcular_max_min_dato', crear una funcion
con la misma lógica la cual reciba un parámetro string que
representará el género del héroe/heroína a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura será similar a la ya
antes creada, salvo que dentro de ella deberá llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
parámetro. Esta función retornará el héroe o heroína que cumpla con

las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
dato)"""

#CALCULA EL MAX O MIN DE LA LISTA QUE INGRESEMOS Y LA KEY QUE SOLICITEMOS DEPENDIENDO SU GENERO
def calcular_max_min_dato_genero(lista_heroes:list,key:str,calculo:str,genero:str):

    if type(lista_heroes) == list and re.search('^minimo$|^maximo$',calculo,re.IGNORECASE):

        calculo = calculo.lower()
        genero = genero.upper()

        valor_retorno = None

        for elemento in lista_heroes:

            if calculo == 'maximo' and elemento['genero'] == genero:

                valor_retorno = calcular_max_genero(lista_heroes,key,genero)

            
            elif elemento['genero'] == genero:

                valor_retorno = calcular_min_genero(lista_heroes,key,genero)

            
        return valor_retorno


""" 3.4. Basandote en la función 'stark_calcular_imprimir_heroe' crear la
función "stark_calcular_imprimir_guardar_heroe_genero" que además
reciba un string el cual representará el género a evaluar. El formato de
mensaje a imprimir deberá ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65
Además la función deberá guardar en un archivo csv el resultado
obtenido.
Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
formato:
heroes_calculo_key_genero.csv
Donde:
● cálculo: representará el string máximo o mínimo
● key: representará cual es la key la cual se tiene que hacer el
cálculo
● genero: representará el género a calcular.
Ejemplo: para calcular el héroe más alto femenino, el archivo se
deberá llamar:
heroes_maximo_altura_F.csv
Esta función retornará True si pudo guardar el archivo, False caso
contrario """

#IMPRIME EL MAX O MIN Y LO GUARDA EN UN ARCHIVO CSV CON EL NOMBRE DE LOS PARAMETROS QUE VAYAMOS INGRESANDO
def stark_calcular_imprimir_heroe_genero(lista_heroes:list,key:str,calculo:str,genero:str):

    if type(lista_heroes) == list:

        valor_heroe = calcular_max_min_dato_genero(lista_heroes,key,calculo,genero)

        valor_para_imprimir = None

        for elemento in lista_heroes:

            if elemento['nombre'] == valor_heroe:

                valor_para_imprimir = obtener_nombre_y_dato(elemento,key)
        

        nombre = f'heroes_{calculo}_{key}_{genero}.csv'

        print(nombre)

        valor_para_guardar = re.sub(r'\|',',',valor_para_imprimir)


        confirmacion_guardado = guardar_archivo(nombre,valor_para_guardar)

        imprimir_dato(valor_para_imprimir)

        return confirmacion_guardado
    

""" 4.1. Basandote en la función 'sumar_dato_heroe', crear la función llamada
'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
del tipo string que representará el género con el que se va a trabajar.
Esta función antes de realizar la suma en su variable sumadora,
deberá validar lo siguiente:

A. El tipo de dato del héroe debe ser diccionario.
B. El héroe actual de la iteración no debe estar vacío (ser
diccionario vacío)
C. El género del héroe debe coincidir con el pasado por
parámetro.

Una vez que cumpla con las condiciones, podrá realizar la suma. La
función deberá retornar la suma del valor de la key de los héroes o
heroínas que cumplan las condiciones o -1 en caso de que no se
cumplan las validaciones """

#SUMA LA CANTIDAD TOTAL DE LA KEY QUE SOLICITEMOS DE LA LISTA SEGUN SU GENERO
def sumar_dato_heroe_genero(lista_heroes:list,key:str,genero:str):

    suma_total = 0

    stark_normalizar_datos(lista_heroes)


    for elemento in lista_heroes:

        if key in elemento and type(elemento) == dict and elemento != '' and elemento['genero'] == genero.upper():

            suma_total += elemento[key]
        
        else:

            valor_retorno = -1


    return suma_total


""" 4.2. Crear la función 'cantidad_heroes_genero' la cual recibirá por
parámetro la lista de héroes y un string que representará el género a
buscar. La función deberá iterar y sumar la cantidad de héroes o
heroínas que cumplan con la condición de género pasada por
parámetro, retornará dicha suma. """

#CUENTA LA CANTIDAD DE HEROES QUE HAY EN LA LISTA SEGUN SU GENERO
def cantidad_heroes_genero(lista_heroes:list,genero:str):

    cantidad_heroes = 0

    for elemento in lista_heroes:

        if elemento['genero'] == genero.upper():

            cantidad_heroes += 1
    

    return cantidad_heroes


""" 4.3. Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro. """

def calcular_promedio_genero(lista_heroes:list,key:str,genero:str):


    suma_total_key = sumar_dato_heroe_genero(lista_heroes,key,genero)

    cantidad_heroes = cantidad_heroes_genero(lista_heroes,genero)

    promedio = dividir(suma_total_key,cantidad_heroes)

    return promedio


""" 4.4. Basandote en la función "stark_calcular_imprimir_promedio_altura",
desarrollar la función 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.
La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:
Altura promedio género F: 178.45
En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.
Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:
heroes_promedio_altura_genero.csv
Donde:
A. genero: será el género de los héroes a calcular, siendo M y F
únicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv

Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta función retornará True si pudo la lista tiene algún elemento y pudo
guardar el archivo, False en caso de que esté vacía o no haya podido
guardar el archivo. """

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,genero:str):


    if len(lista_heroes) > 0:

        promedio = calcular_promedio_genero(lista_heroes,'altura',genero)

        mensaje = f'Altura promedio genero {genero.upper()}: {promedio}'

        imprimir_dato(mensaje)

        nombre = f'heroes_promedio_altura_{genero.upper()}.csv'

        confirmacion_guardado = guardar_archivo(nombre,mensaje)
    
    else:

        imprimir_dato('Error: Lista de heroes vacia.')

    
    return confirmacion_guardado


""" 5.1. Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)
Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
de estarlo devolver un diccionario con la siguiente estructura:

{
"Error": “La lista se encuentra vacía”
}

La función deberá retornar un diccionario con los distintos valores del
tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
diccionario clave valor).
Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un
diccionario de la siguiente manera:

{
"Celeste": 4,
"Verde": 8,
"Marron": 6
}

Reutilizar la función 'capitalizar_palabras' para capitalizar los valores
de las keys. """

#calcula la cantidad de heroes en cada tipo de color de ojos o pelo y retorna todos los valores en un diccionario
def calcular_cantidad_tipo(lista_heroes:list,key:str)->dict:

    if len(lista_heroes) > 0:

        diccionario_datos = {}

        set_colores = set()


        #RECORRO TODA LA LISTA PARA OBTENER LOS COLORES
        for elemento in lista_heroes:

            if key in elemento:

                set_colores.add(elemento[key].lower())

        #RECORRO LOS COLORES Y LUEGO LA LISTA DE HEROES PARA COMPARAR Y EN CASO QUE SI LE SUMO UNO Y LO AGREGO AL DICCIONARIO
        for color in set_colores:

            cantidad_color = 0

            for heroe in lista_heroes:

                if color == heroe[key].lower():

                    cantidad_color += 1
            #utilizo la funcion capitalizar para cada color inicie con una mayuscula
            diccionario_datos[capitalizar_palabras(color)] = cantidad_color


        valor_retorno = diccionario_datos

    else:

        diccionario = {'Error:':'La lista se encuentra vacia'}

        valor_retorno = diccionario

    return valor_retorno



""" 5.2. Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como
parámetro un diccionario que representará las distintas variedades del
tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
respectivas cantidades como valor. Como segundo parámetro recibirá
el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo
únicamente en el mensaje final formateado. Esta función deberá iterar
cada key del diccionario y variabilizar dicha key con su valor para
luego formatearlos en un mensaje el cual deberá guardar en archivo.
Por ejemplo:

"Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
Reutilizar la función 'guardar_archivo'. El nombre del archivo final
deberá respetar el formato:
heroes_cantidad_tipoDato.csv
Donde:
● tipoDato: representará el nombre de la key la cual se está
evaluando la cantidad de héroes.
Ejemplo:
heroes_cantidad_color_pelo.csv
heroes_cantidad_color_ojos.csv
La función retornará True si salió todo bien, False caso contrario. """

#IMPRIME Y GUARDA EN UN ARCHIVO CSV LA CANTIDAD DE HEROES CON EL MISMO COLOR DE PELO O OJOS DEPENDE LA KEY INGRESADA
def guardar_cantidad_heroes_tipo(heroe:dict,key:str):

    mensaje = ""

    #RECORRO EL DICCIONARIO Y ACCEDO A LA KEY Y EL VALUE
    for clave,valor in heroe.items():

        mensaje += f'{key} {clave} - Cantidad de heroes: {valor} \n'

    print(mensaje)

    nombre_archivo = f'heroes_cantidad_{key}.csv'

    valor_funcion = guardar_archivo(nombre_archivo,mensaje)

    return valor_funcion



""" 5.3. Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
la lógica que cada una de esas funciones manejan.
Esta función retornará True si pudo guardar el archivo, False caso
contrario. """
#ESTA FUNCION LLAMA LAS DOS ANTERIORES Y LAS COMBINA, CALCULA LA CANTIDAD DE CADA TIPO Y LAS IMPRIME Y GUARDA 
def stark_calcular_cantidad_por_tipo(lista_heroes:list,key:str):

    dict_datos = calcular_cantidad_tipo(lista_heroes,key)

    valor = guardar_cantidad_heroes_tipo(dict_datos,key)

    return valor


""" 6.1. Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc).
Esta función deberá iterar la lista de héroes guardando en una lista las
variedades del tipo de dato pasado por parámetro (sus valores).
En caso de encontrar una key sin valor (o string vacío), deberás
hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
guardando todos los valores encontrados, si el valor del héroe no tiene
errores, guardarlo tal cual viene.
Finalmente deberás eliminar los duplicados de esa lista y retornarla

como un set.
Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
con la primera letra mayúscula. """

#OBTENEMOS EL TIPO DE CADA COLOR DE PELO POR EJEMPLO Y LO RETORNA EN UN SET
def obtener_lista_de_tipos(lista_heroes:list,key:str)->set:

    lista_datos = []

    for elemento in lista_heroes:

        if elemento[key] != '' and key in elemento:

            lista_datos.append(capitalizar_palabras(elemento[key]))

        else:

            lista_datos.append('N/A')

    #lo paso a un set para que no se repita

    lista_datos = set(lista_datos)

    return lista_datos

""" 6.2. Crear la función 'normalizar_dato' la cual recibirá por parámetro un
dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representará el valor por defecto a colocar
en caso de que el valor está vacío. Deberá validar que el dato no esté
vacío, en caso de estarlo lo reemplazará con el valor default pasado
por parámetro y lo retornará, caso contrario lo retornará sin
modificaciones. """

#NORMALIZA UNA PALABRA DEVUELVE EL DATO INGRESADO Y EN CASO DE SER UNA CADENA VACIA LA RETORNA CON 'N/A' 
def normalizar_dato(dato:str,valor_defecto:str):

    if dato != "":

        valor_retorno = dato

    else:
        
        valor_retorno = valor_defecto

    return valor_retorno

""" 6.3. Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
primero será un diccionario que representará un solo héroe, el
segundo parámetro será el nombre de la key de dicho diccionario la
cual debe ser normalizada.
La función deberá capitalizar las palabras que tenga dicha key como
valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
que setearlo con N/A).
Finalmente deberá capitalizar todas las palabras del nombre del héroe
y deberá retornar al Hero con cada palabra de su nombre
capitalizados, cada palabra del valor de la key capitalizadas y
normalizadas (con N/A en caso de que estuviesen vacías por defecto).
Reutilizar: 'capitalizar_palabras' y 'normalizar_dato' """

#NORMALIZA EL DATO DE UN DICCIONARIO Y LES AGREGA MAYUSCULA A CADA INICIAL, RETORNA LA PALABRA NORMALIZADA
def normalizar_heroe(heroe:dict,key:str):

    palabra = heroe[key]

    if heroe[key] != "":

        palabra = capitalizar_palabras(heroe[key])

    palabra_normalizada = normalizar_dato(palabra,'N/A')

    return palabra_normalizada



""" 6.4. Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por
parámetro:
A. La lista de héroes
B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
C. El tipo de dato a evaluar (la key en cuestion, color_ojos,
color_pelo, etc)
PRESTAR ATENCIÓN:

A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar
si ese tipo existe como key en un diccionario el cual deberás armar.
(contendrá cada variedad como key y una lista de nombres de héroes
como valor de cada una de ellas).
B. En caso de no existir dicha key en el diccionario, agregarla con una
lista vacía como valor.
C. Dentro de la iteración de variedades, iterar la lista de héroes (for
anidado) 'normalizando' el posible valor que tenga la key evaluada, ya
que podría venir vacía (qué función usarias aca? guiño guiño)
D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo
pasado por parámetro.
E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la
variedad iterada en el primer bucle.
Esta función retornará un diccionario con cada variedad como key y
una lista de nombres como valor.
Por ejemplo:

{
"Celestes": ["Capitan America", "Tony Stark"],
"Verdes": ["Hulk", "Viuda Negra"]
....
}  """
#OBTIENE LOS NOMBRES DE CADA HEROES QUE TIENE CADA COLOR DE PELO O OJOS Y LOS GUARDA EN UN DICCIONARIO QUE DENTRO CONTIENE UNA LISTA CON LOS NOMBRES
def obtener_heroes_por_tipo(lista_heroes:list,tipo_variedades:set,key:str)->dict:

    diccionario_nuevo = {}

    for color in tipo_variedades:

        lista_nombre = []

        for heroe in lista_heroes:

            if key in heroe:

                color_heroe = normalizar_heroe(heroe,key)

                if color_heroe.lower() == color.lower():

                    lista_nombre.append(heroe['nombre'])
                
        
        diccionario_nuevo[color] = lista_nombre


    return diccionario_nuevo



""" 6.5. Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por
parámetro un diccionario que representará los distintos tipos como
clave y una lista de nombres como valor (Lo retorna la función anterior)
y además como segundo parámetro tendrá un string el cual
representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
Deberá recorrer cada key y cada valor (lista) que esta contenga para
finalmente crear un string el cual será un mensaje que deberás
imprimir formateado.
Por ejemplo:
"color_ojos Green: Black Widow | Hulk"
Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar
el formato:
heroes_segun_TipoDato.csv
Donde:
● TipoDato: es la key la cual indicará qué cosas se deben guardar
en el archivo.
Ejemplo:
heroes_segun_color_pelo.csv (Agrupados por color de pelo)
heroes_segun_color_ojos.csv (Agrupados por color de ojos)
Esta función retorna True si salió todo bien, False caso contrario. """

#IMPRIME POR PANTALLA TODOS LOS HEROES SEGUN SU COLOR DE PELO O OJOS, Y LOS GUARDA EN UN ARCHIVO CSV
def guardar_heroes_por_tipo(heroe:dict,key:str)->bool:

    mensaje = ""

    for clave,valor in heroe.items():

        mensaje += key +' '+ clave+': '+ ' | '.join(valor)+'\n'
        
    print(mensaje)

    nombre_archivo = f'heroes_segun_{key}.csv'

    confirmacion = guardar_archivo(nombre_archivo,mensaje)

    return confirmacion



""" 6.6. Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar
las funciones:
A. 'obtener_lista_de_tipos'
B. 'obtener_heroes_por_tipo'
C. 'guardar_heroes_por_tipo'
Pasando por parámetro lo que corresponda según la lógica de las
funciones usadas.

Esta función retornará True si pudo guardar el archivo, False caso
contrario. """


def stark_listar_heroes_por_dato(lista_heroes:list,key:str)->bool:

    tipo = obtener_lista_de_tipos(lista_heroes,key)                  
    valor = obtener_heroes_por_tipo(lista_heroes,tipo,key)
    confirmacion = guardar_heroes_por_tipo(valor,key)

    return confirmacion

stark_listar_heroes_por_dato(lista_personajes,'color_ojos')
                


            
            


