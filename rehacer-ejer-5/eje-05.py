import re

from data_stark import lista_personajes

""" 1.1. Crear la función "extraer_iniciales" que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)
● En el caso que el nombre del personaje contenga el artículo "the" se
deberá omitir de las iniciales
● Se deberá verificar si el nombre contiene un guión "-" y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
● Que el string recibido no se encuentre vacío
Devolver "N/A" en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D. """

def extraer_iniciales(nombre_heroe:str)->str:

    if type(nombre_heroe) == str:

        nombre_heroe = nombre_heroe.strip()

        nombre_heroe = nombre_heroe.upper()

        nombre_heroe = re.sub('-',' ',nombre_heroe)

        nombre_heroe = re.sub('THE','',nombre_heroe)

        nombre_heroe = nombre_heroe.split(' ')

        iniciales = ""

        for letra in nombre_heroe:

            if letra != '':
                iniciales += letra[0] + '.'

        valor_retorno = iniciales

    else:

        valor_retorno = 'N/A'

    return valor_retorno



""" 1.2. Crear la función "definir_iniciales_nombre" la cual recibirá como parámetro:
● heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar "iniciales" y su valor será el obtenido de
llamar a la función "extraer_iniciales"
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave "nombre"
En caso de encontrar algún error retornar False, caso contrario retornar True """
                    
def definir_iniciales_nombre(heroe:dict):

    if type(heroe) == dict and 'nombre' in heroe:

    
        heroe['iniciales'] = extraer_iniciales(heroe['nombre'])

        valor_retorno = True
    
    else:

        valor_retorno = False
    
    return valor_retorno


""" 1.3. Crear la función "agregar_iniciales_nombre" la cual recibirá como
parámetro:
● lista_heroes: lista de personajes
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función
definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se
deberá detener la iteración e informar por pantalla el siguiente mensaje:
"El origen de datos no contiene el formato correcto"
La función deberá devolver True en caso de haber finalizado con éxito o False
en caso de que haya ocurrido un error """


def agregar_iniciales_nombre(lista_heroes:list):

    if type(lista_heroes) == list and len(lista_heroes) > 0:

        valor_retorno = True

        for heroe in lista_heroes:

            valor = definir_iniciales_nombre(heroe)

            if valor == False:

                print('El origen de datos no contiene el formato correcto')
                valor_retorno = False
                break
        

        return valor_retorno
    

""" 1.3. Crear la función "stark_imprimir_nombres_con_iniciales" la cual recibirá
como parámetro:
● lista_heroes: la lista de personajes
La función deberá utilizar la función "agregar_iniciales_nombre" para añadirle
las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes
seguido de las iniciales encerradas entre paréntesis ()
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco "*" (de forma de
viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
...
La función no retorna nada """

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    if type(lista_heroes) == list and len(lista_heroes) > 0:

        valor = agregar_iniciales_nombre(lista_heroes)

        if valor == True:

            nombre_con_abreviatura = ""

            for heroe in lista_heroes:

                nombre_con_abreviatura += '* '+ heroe['nombre'] +' '+'('+heroe['iniciales']+')\n'
            
            print(nombre_con_abreviatura)


""" 2.1. Crear la función "generar_codigo_heroe" la cual recibirá como parámetros:
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
● genero_heroe: un string que representa el género del héroe ( puede
tomar los valores "M", "F" o "NB")

La función deberá generar un string con el siguiente formato:
GENERO-000...000ID
Es decir, el género recibido por parámetro seguido de un "-" (guión) y por
último el identificador recibido. Todos los códigos generados deben tener
como máximo 10 caracteres (contando todos los caracteres, inclusive el
guión). Se deberá completar con ceros para que todos queden del mismo
largo
Algunos ejemplos:
F-00000001
M-00000002
NB-0000010
La función deberá validar:
● El identificador del héroe sea numérico.
● El género no se encuentre vacío y este dentro de los valores esperados
("M", "F" o "NB")
En caso de no pasar las validaciones retornar "N/A". En caso de verificarse
correctamente retornar el código generado """

def generar_codigo_heroe(id_heroe:int,genero_heroe:str):

    if type(id_heroe) == int and re.search('^[fm]$|^nb$',genero_heroe,re.IGNORECASE):

        id_heroe = str(id_heroe)

        if genero_heroe.lower() == 'nb':

            codigo = id_heroe.zfill(7)
        
        else:

            codigo = id_heroe.zfill(8)

        codigo_completo = genero_heroe.upper() +'-'+codigo

        valor_retorno = codigo_completo

    else:

        valor_retorno = 'N/A'


    return valor_retorno

""" 2.2. Crear la función "agregar_codigo_heroe" la cual recibirá como parámetro:
● heroe: un diccionario con los datos del personaje
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero

La función deberá agregar una nueva clave llamada "codigo_heroe" al
diccionario "heroe" recibido como parámetro y asignarle como valor un código
utilizando la función "generar_codigo_heroe"
La función deberá validar:
● Que el diccionario recibido como parámetro no se encuentre vacío.
● Que el código recibido mediante generar_codigo_heroe tenga
exactamente 10 caracteres
En caso de pasar las validaciones correctamente la función deberá retornar
True, en caso de encontrarse un error retornar False """

def agregar_codigo_heroe(heroe:dict,id_heroe:int):

    if type(heroe) == dict:

        codigo = generar_codigo_heroe(id_heroe,heroe['genero'])

        if len(codigo) == 10:

            heroe['codigo_heroe'] = codigo

            valor_retorno = True
    
    else:

        valor_retorno = False

    return valor_retorno

""" 2.3. Crear la función "stark_generar_codigos_heroes" la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y agregarle el código a cada
uno de los personajes.
El código del héroe (id_heore) surge de la posición del mismo dentro de la
lista_heroes (comenzando por el 1).
Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
héroe que se está iterando y el id_heroe
Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
(## representa la cantidad de códigos generados):
Se asignaron ## códigos
* El código del primer héroe es: M-00000001

* El código del del último héroe es: M-00001224
La función deberá validar::
● La lista contenga al menos un elemento
● Todos los elementos de la lista sean del tipo diccionario
● Todos los elementos contengan la clave "genero"
En caso de encontrar algún error, informar por pantalla: "El origen de datos no
contiene el formato correcto"
La función no retorna ningún valor. """

def stark_generar_codigos_heroes(lista_heroes:list):

    if len(lista_heroes) > 0:

        contador = 0

        mensaje= ""

        for heroe in lista_heroes:

            contador +=1

            if type(heroe) == dict and 'genero' in heroe:

                valor = agregar_codigo_heroe(heroe,contador)

                mensaje += '* El codigo del heroe '+heroe['nombre']+' es: '+heroe['codigo_heroe']+'\n'

        
        if valor == True:

            print('Se asignaron '+str(contador)+' codigos\n'+mensaje)

        else:

            print('El origen de datos no contiene el formato correcto')
            
    
    else:

        print('El origen de datos no contiene el formato correcto')


""" 3.1. Crear la función "sanitizar_entero" la cual recibirá como parámetro:
● numero_str: un string que representa un posible número entero
La función deberá analizar el string recibido y determinar si es un número
entero positivo. La función debe devolver distintos valores según el problema
encontrado:
● Si contiene carácteres no numéricos retornar -1
● Si el número es negativo se deberá retornar un -2
● Si ocurren otros errores que no permiten convertirlo a entero entonces
se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string
en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número
entero positivo, retornarlo convertido en entero """

def sanitizar_entero(numero_str:str):

    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if re.search('^[0-9]+$',numero_str):

            numero_str = int(numero_str)

            valor_retorno = numero_str

        elif re.search('^-[0-9]+$',numero_str):

            valor_retorno = -2

        elif re.search('[^0-9+$]',numero_str):

            valor_retorno = -3

    return valor_retorno

""" 3.2. Crear la función "sanitizar_flotante" la cual recibirá como parámetro:
● numero_str: un string que representa un posible número decimal
La función deberá analizar el string recibido y determinar si es un número
flotante positivo. La función debe devolver distintos valores según el
problema encontrado:

● Si contiene carácteres no numéricos retornar -1
● Si el número es negativo se deberá retornar un -2
● Si ocurren otros errores que no permiten convertirlo a entero entonces
se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string
en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número
flotante positivo, retornarlo convertido en flotante """

def sanitizar_flotante(numero:str):

    if type(numero) == str:
        numero = numero.strip()

        if re.search('^[0-9]+\.[0-9]+$',numero):

            numero = float(numero)

            valor_retorno = numero

        elif re.search('^-[0-9]+\.[0-9]+$',numero):

            valor_retorno = -2
        
        elif re.search('[^0-9+\.0-9+$]',numero):

            valor_retorno = -1
        
        else:
            valor_retorno = -3

    return valor_retorno


""" 3.3. Crear la función "sanitizar_string" la cual recibirá como parámetro
● valor_str: un string que representa el texto a validar
● valor_por_defecto: un string que representa un valor por defecto
(parámetro opcional, inicializarlo con "-")
La función deberá analizar el string recibido y determinar si es solo texto (sin
números). En caso de encontrarse números retornar “N/A”
En el caso que valor_str contenga una barra "/" deberá ser reemplazada por un
espacio
El espacio es un caracter válido
En caso que se verifique que el parámetro recibido es solo texto, se deberá
retornar el mismo convertido todo a minúsculas
En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
un valor por defecto, entonces retornar el valor por defecto convertido a
minúsculas
Quitar los espacios en blanco de atras y adelante de ambos parámetros en
caso que los tuviese """

def sanitizar_string(valor_str:str,valor_por_defecto ='-'):

    valor_retornar = ""

    if type(valor_str) == str:

        if re.search('^[a-z]+/?\s?[a-z]+$',valor_str,re.IGNORECASE):

            valor_str = re.sub('/',' ',valor_str)
            valor_str = valor_str.strip()

            valor_retornar = valor_str.lower()
        
        elif re.search('[0-9]+',valor_str):

            valor_retornar = "N/A"


        elif valor_str == "":

            valor_retornar = valor_por_defecto.lower()

    return valor_retornar


""" 3.4. Crear la función "sanitizar_dato" la cual recibirá como parámetros:
● heroe: un diccionario con los datos del personaje
● clave: un string que representa el dato a sanitizar (la clave del
diccionario). Por ejemplo altura
● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
tomar los valores: "string", "entero" y "flotante"
La función deberá sanitizar el valor del diccionario correspondiente a la clave
y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los
puntos 3.1, 3.2, 3.3 y 3.4

Se deberá validar:
● Que tipo_dato se encuentre entre los valores esperados ("string, "entero,
"flotante)" la validación debe soportar que nos lleguen mayúsculas o
minúsculas. En caso de encontrarse un valor no válido informar por
pantalla: "Tipo de dato no reconocido"

● Que clave exista como clave dentro del diccionario heroe. En caso de
no encontrarse, informar por pantalla: "La clave especificada no
existe en el héroe". (en este caso la validación es sensible a
mayúsculas o minúsculas)
Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y
False en caso contrario. """

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):

    valor_retorno = False

    if re.search('^string$|^entero$|^flotante$',tipo_dato,re.IGNORECASE):

        if clave in heroe:
            
            tipo_dato = tipo_dato.lower()

            if tipo_dato == "string":

                heroe[clave] = sanitizar_string(heroe[clave])

            elif tipo_dato == "entero":

                heroe[clave] = sanitizar_entero(heroe[clave])
            
            else:

                heroe[clave] = sanitizar_flotante(heroe[clave])

            valor_retorno = True
    else:

        print('Tipo de dato no reconocido')

    return valor_retorno

""" 3.5. Crear la función "stark_normalizar_datos" la cual recibirá como
parámetros:
● lista_heroes: la listas personajes
La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
siguientes claves: "altura", "peso", "color_ojos", "color_pelo", "fuerza" e
"inteligencia"
● Un vez finalizado el proceso mostrar el mensaje "Datos normalizados",
● Validar que la lista de héroes no esté vacía para realizar sus acciones,
caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
● La función no retorna nada
● Reutilizar la función sanitizar_dato """

def stark_normalizar_datos(lista_heroes:list):

    if len(lista_heroes) > 0:

        lista_para_sanitizar= ["altura", "peso", "color_ojos", "color_pelo", "fuerza", "inteligencia"]
        tipo_dato_sanitizar = ["flotante","flotante","string","string","entero","string"]

        for clave,dato in zip(lista_para_sanitizar,tipo_dato_sanitizar):
        
            for heroe in lista_heroes:

                valor = sanitizar_dato(heroe,clave,dato)

        print('Datos normalizados')

        return valor
    
""" 4.1. Crear la función "generar_indice_nombres" la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y generar una lista donde cada
elemento es cada palabra que componen el nombre de los personajes.
Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
["Howard", "the", "Duck", "Rocket", "Raccoon", "Wolverine", … ]
La función deberá validar que:
● La lista contenga al menos un elemento
● Todos los elementos de lista_heroes sean del tipo diccionario
● Todos los elementos contengan la clave "nombre"

En caso de encontrar algún error, informar por pantalla: "El origen de datos no
contiene el formato correcto" """

def generar_indice_nombres(lista_heroes:list):

    if len(lista_heroes) > 0:

        lista_palabras_nombre = []

        for heroe in lista_heroes:

            if 'nombre' in heroe and type(heroe) == dict:

                heroe['nombre']= re.sub('-',' ',heroe['nombre'])

                palabra_dividida = re.split(' ',heroe['nombre'])

                lista_palabras_nombre.extend(palabra_dividida)

        return lista_palabras_nombre

""" 4.2. Crear la función "stark_imprimir_indice_nombre" la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá mostrar por pantalla el índice generado por la función
generar_indice_nombres con todos los nombres separados con un guión.
Por ejemplo:
Howard-the-duck-Rocket-Raccoon-Wolverine… """

def stark_imprimir_indice_nombre(lista_heroes:list):

    lista = generar_indice_nombres(lista_heroes)

    mensaje = ""

    for i in lista:

        mensaje += i + '-'

    print(mensaje[:-1])


