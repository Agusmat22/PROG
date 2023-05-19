from data_stark import lista_personajes

import re

""" Desafío #02: (con biblioteca propia: stark_biblioteca)
En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones. Es por ello que te proponemos lo siguiente:
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!


0.0
Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
Si al menos un dato fue modificado, la función deberá imprimir como mensaje "Datos normalizados", caso contrario no imprimirá nada.
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía” """

#TRANSFORMA DE STR A INT O FLOAT LAS ALTURAS,PESOS Y FUERZA
def stark_normalizar_datos(lista_heroes:list):

    valor_retornado = ""

    if len(lista_heroes) > 0:

        for elemento in lista_heroes:

            if type(elemento['altura']) == str:

                elemento['altura'] = float(elemento['altura'])

                valor_retornado = "Datos Normalizados"

            if type(elemento['peso']) == str:

                elemento['peso'] = float(elemento['peso'])

                valor_retornado = "Datos Normalizados"
            
            if type(elemento['fuerza']) == str:

                elemento['fuerza'] = int(elemento['fuerza'])
            
                valor_retornado = "Datos Normalizados"

    else:

        valor_retornado = "ERROR: Lista vacia"
    

    if valor_retornado != "":

        print(valor_retornado)


""" 
1.1 
Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y 
devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
Nombre: Howard the Duck
 
"""
#OBTIENE EL NOMBRE DE UN DICCIONARIO
def obtener_nombre(heroe:dict):

    nombre_heroe = ""

    nombre_heroe = 'Nombre: '+ heroe['nombre']

    return nombre_heroe


""" 
1.2
Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.
"""
#IMPRIME POR CONSOLA EL STR INGRESADO, NO RETORNA
def imprimir_dato(dato:str):

    print(dato)

""" 
1.3
Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Con este se resuelve el Ej 1 del desafío #00
"""

def stark_imprimir_nombres_heroes(lista_heroes:list):

    if len(lista_heroes) > 0:

        for elemento in lista_heroes:

            valor_nombre = obtener_nombre(elemento)
            imprimir_dato(valor_nombre)

    

    else:

        return -1
    

"""
2.
Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 


La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500

"""

def obtener_nombre_y_dato(heroe:dict,key:str):

    if type(heroe) == dict:

        nombre = obtener_nombre(heroe)

        key_elegida = " | "

        key_elegida += (f'{key} : {heroe[key]}')

        valor_concatenado = nombre + key_elegida

        return valor_concatenado

"""
4.1
Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) 
la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. 
Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
Ejemplo de llamada:

calcular_max(lista, 'edad')
"""
#CALCULA EL MAXIMO DE CUALQUIER KEY QUE SEA DE TIPO NUMERICO
def calcular_max(lista_heroes:list,key:str):

    if type(lista_heroes) == list:

        stark_normalizar_datos(lista_heroes)

        #creo el maximo y ya lo inicializo
        valor_max = None

        nombre_heroe_max_altura = None

        valor_max = lista_heroes[0][key]

        for elemento in lista_heroes:

            if elemento[key] > valor_max:

                valor_max = elemento[key]
                
                nombre_heroe_max_altura = elemento['nombre']
        
        return nombre_heroe_max_altura
    
"""
4.2

Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string)
la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. 
Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo.
Ejemplo de llamada:

calcular_min(lista, 'edad')

"""
#CALCULA EL MINIMO DE CUALQUIER KEY QUE SEA DE TIPO NUMERICO
def calcular_min(lista_heroes:list,key:str):

    if type(lista_heroes) == list:

        stark_normalizar_datos(lista_heroes)

        #creo el minimo y ya lo inicializo
        valor_min = None

        nombre_heroe_min_altura = None

        valor_min = lista_heroes[0][key]

        nombre_heroe_min_altura = lista_heroes[0]['nombre']

        for elemento in lista_heroes:

            if valor_min > elemento[key]:

                valor_min = elemento[key]
                
                nombre_heroe_min_altura = elemento['nombre']

        
        return nombre_heroe_min_altura

"""
4.3

Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:

La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores "maximo" o "minimo"
Un string que representa la key del dato a calcular, por ejemplo: "altura", "peso", "edad", etc.
La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
Ejemplo de llamada:
calcular_max_min_dato(lista, "maximo", "edad")
"""

#SEGUN EL VALOR(MAXIMO O MINIMO) INGRESADO VA LLAMAR A LA FUNCIONES ANTERIORES Y RETORNA EL VALOR
def calcular_max_min_dato(lista_heroes:list,calculo:str,key:str):

    if type(lista_heroes) == list and re.search('^maximo$|^minimo$',calculo,re.IGNORECASE ):

        
        if calculo.lower() == "maximo":

            valor_retornado = calcular_max(lista_heroes,key)
        
        else:

            valor_retornado = calcular_min(lista_heroes,key)

        return valor_retornado

"""
4.4

Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 

La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores "maximo" o "minimo"
Un string que representa la key del dato a calcular, por ejemplo: "altura", "peso", "edad", etc.
Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
punto 1.2, punto: 2 y punto 4.3 
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Ejemplo de llamada:
 	stark_calcular_imprimir_heroe (lista, "maximo", "edad")
            Ejemplo de salida:
	Mayor altura: Nombre: Howard the Duck | altura: 79.34
"""

def stark_calcular_imprimir_heroe(lista_heroes:list,calculo:str,key:str):

    if type(lista_heroes) == list and re.search('^maximo$|^minimo$',calculo,re.IGNORECASE ):

        valor_heroe = calcular_max_min_dato(lista_heroes,calculo,key)

        nombre_y_dato = None
                
        for elemento in lista_heroes:

            if elemento['nombre'] == valor_heroe:

                nombre_y_dato = obtener_nombre_y_dato(elemento,key)
                
        if calculo.lower() == "maximo":

            print(f'Mayor {key}: {nombre_y_dato}')

        else:

            print(f'Menor {key}: {nombre_y_dato}')



"""5.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes 
y un string que representara el dato/key de los héroes que se requiere sumar. 
Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. 
La función deberá retorna la suma de todos los datos según la key pasada por parámetro """

def sumar_dato_heroe(lista_heroes:list,key:str):

    if type(lista_heroes) == list:

        stark_normalizar_datos(lista_heroes)

        suma = 0

        for elemento in lista_heroes:

            if type(elemento) == dict and elemento != '' and key in elemento:

                suma += elemento[key]

        return suma

a = sumar_dato_heroe(lista_personajes,'peso')
print(a)

"""5.2 Crear la función  "dividir" la cual recibirá como parámetro dos números (dividendo y divisor).
Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar la división 
entre los parámetros y retornar el resultado """


def dividir(dividendo:float,divisor:int):

    if divisor != 0:

        valor_retornado = dividendo / divisor

    else:

        valor_retornado = 0
    
    return valor_retornado

"""5.3 Crear la función 'calcular_promedio' la cual recibirá como parámetro una lista de héroes y
un string que representa el dato del héroe que se requiere calcular el promedio.
La función debe retornar el promedio del dato pasado por parámetro """

def calcular_promedio(lista_heroes:list,key:str):

    if type(lista_heroes) == list and re.search(f'^[a-z]+$',key,re.IGNORECASE):

        suma_dato_solicitado = sumar_dato_heroe(lista_heroes,key)

        contador_heroes_key = 0

        for elemento in lista_heroes:

            if key in elemento:

                contador_heroes_key += 1

        
        promedio_dato = dividir(suma_dato_solicitado,contador_heroes_key)

        return promedio_dato

"""5.4 Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y 
utilizando la función del punto 5.3 calcula y mostrará la altura promedio. 
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
 """

def stark_calcular_imprimir(lista_heroes:list):

    if len(lista_heroes) > 0:

        valor = calcular_promedio(lista_heroes,'altura')
        
        imprimir_dato(valor)

    else:

        return -1
    
