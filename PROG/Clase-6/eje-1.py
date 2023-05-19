from data_stark import lista_personajes

#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS

#importo la biblioteca de exrepesiones regulares
import re


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

def extraer_iniciales(nombre_heroe:str):

    if type(nombre_heroe) == str and nombre_heroe != "":

        nombre_ingresado = nombre_heroe

        nombre_ingresado = nombre_ingresado.upper()

        #utilizo los metodos de la biblioteca de expresiones regulares
        #re.sub reemplaza el primer valor por el segundo
        nombre_ingresado = re.sub('-',' ',nombre_ingresado)
        
        nombre_ingresado = re.sub('THE','',nombre_ingresado)

        #divido en listas el nombre
        nombre_ingresado = re.split(' ', nombre_ingresado)

        nombre_abreviado = ""

        #recorro el caracter y agarro el primer valor
        for caracter in nombre_ingresado:
        
            if caracter != "":
                nombre_abreviado += caracter[0] + "."


        return nombre_abreviado

    else:

        return "N/A"



"""1.2. Crear la función "definir_iniciales_nombre" la cual recibirá como parámetro:
● heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar "iniciales" y su valor será el obtenido de
llamar a la función "extraer_iniciales"
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave "nombre"
En caso de encontrar algún error retornar False, caso contrario retornar True  """


def definir_iniciales_nombre(heroe:dict):

    if type(heroe) == dict and 'nombre' in heroe:

        heroe['iniciales'] = extraer_iniciales(heroe['nombre'])

        return True

    else:

        return False



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

        for elemento in lista_heroes:

            valor_retorno = definir_iniciales_nombre(elemento)

            if valor_retorno == False:

                print("El origen de datos no contiene el formato correcto")
                break
                
                
        
        if valor_retorno == True:
            return True
        
        else:
            return False
        
    else:

        return False


""" 1.3. Crear la función "stark_imprimir_nombres_con_iniciales" la cual recibirá
como parámetro:
● lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre" para añadirle
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

        agregar_iniciales_nombre(lista_heroes)

        for elemento in lista_heroes:

            print("* "+ elemento['nombre'],elemento['iniciales'])


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

    if type(id_heroe) == int and genero_heroe == "M" or genero_heroe == "F"        or genero_heroe == "NB":

        id_heroe = str(id_heroe)

        if genero_heroe == "NB":

            codigo = id_heroe.zfill(7)
        
        else:

            codigo = id_heroe.zfill(8)

        codigo_completo = genero_heroe+'-'+codigo


        return codigo_completo




    else:

        return "N/A"

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

    if len(heroe) > 0:

        heroe['genero'] = heroe['genero'].upper()

        codigo = generar_codigo_heroe(id_heroe,heroe['genero'])

        if len(codigo) == 10:

            heroe['codigo_heroe'] = codigo
            
            return True
        
        else:

            return False

    else:

        return False
    

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

        for diccionario in lista_heroes:

            if type(diccionario) != dict and 'genero' not in diccionario:

                print("El origen de datos no contiene el formato correcto")

            else:

                cantidad_heroes = len(lista_heroes)

                for posicion in range(cantidad_heroes):

                    agregar_codigo_heroe(lista_heroes[posicion],posicion)

                
        print('(# representa la cantidad de codigos generados) \n'
                'Se aginaron'+str(cantidad_heroes)+' codigos\n'
            )

        for posicion in range(cantidad_heroes):
            print('* El codigo del heroe', posicion,'es:',lista_heroes[posicion]['codigo_heroe'])
                

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
    
    """ EXPRESIONES REGULARES PARA CADA VALIDACION

        QUITAR ESPACIOS EN BLANCO DE ADELANTE Y AL FINAL DE LA CADENA

        re.sub(^\s+|\s+$)

        ^\s+ = Si empieza con un espacio en blanco o mas  

        | = es OR para dividir uno u otro


        re.match('valor a buscar', variable o parametro)

        si encuentra el valor buscado devuelve un match y sino devuelve None

        SEARCH Y MATCH SON MUY PARECIDOS

        NUMERO NEGATIVO USANDO IF

        ^- = pregunto si la cadena empieza con un guion solo

        \d+ = pregunto si continua con uno o mas digitos por eso se agrega el mas, sino unicamente estariamos preguntando por el primer digito

        $ = lo coloco post \d+ para asegurar que la cadena finalize con numeros

      
        """
    
    if type(numero_str) == str:


        numero_str = re.sub("^\s+|\s+$", "", numero_str)

        #Numero Positivo
        if re.search('^\d+$', numero_str):

            numero_entero = int(numero_str)

            valor_retorno = numero_entero
            
        #numero negativo
        elif re.search('^-\d+$', numero_str):

            valor_retorno = -2

        #Caracteres no numericos
        elif re.search('.',numero_str):

            valor_retorno = -1
        
        #Otro tipo de errores
        else:

            valor_retorno = -3
    
    else:

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


def sanitizar_flotante(numero_str:str):

    if type(numero_str) == str and numero_str != "":

        #saco los espacios en blanco al principio y final
        numero_str = re.sub('^\s+|\s+$', "", numero_str)

        #numero positivo flotante
        if re.search('^\d+\.\d+$', numero_str):

            numero_flotante = float(numero_str)

            valor_retorno = numero_flotante
        
        #numero negativo flotante
        elif re.search('^-\d+\.\d+$', numero_str):

            valor_retorno = -2
        
        else:
            #caracter no numerico por descarte
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

def sanitizar_string(valor_str:str,valor_por_defecto ="-"):

    if type(valor_str) == str and type(valor_por_defecto) == str:

        #reemplazo los espacios vacios del principio y final
        valor_str = re.sub("^\s+|\s+$", "", valor_str)

        #reemplazo los espacios vacios del principio y final
        valor_por_defecto = re.sub("^\s+|\s+$", "", valor_por_defecto)

        valor_str = re.sub("/", " ", valor_str)


        #Busco si la cadena contiene algun numero
        if re.search('[0-9]', valor_str):

            valor_retorno = "N/A"
        

        #la cadena no contiene numeros, paso el str a minuscula y lo retorno
        else:
            
            valor_minusculas = valor_str.lower()

            valor_retorno = valor_minusculas
            


        if valor_str == "":

            valor_retorno = valor_por_defecto

    
        return valor_retorno
    


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

    #HEROE  un diccionario con los datos del personaje
    #CLAVE  un string que representa el dato a sanitizar (la clave del diccionario). Por ejemplo altura
    #representa el tipo de dato a sanitizar. Puede tomar los valores: "string", "entero" y "flotante"

    if type(heroe) == dict and type(clave) == str and type(tipo_dato) == str:

        if clave in heroe:

            if tipo_dato.lower() == "string" or tipo_dato.lower() == "entero" or tipo_dato.lower() == "flotante":

                if tipo_dato.lower() == "string":

                    heroe[clave] = sanitizar_string(heroe[clave],heroe[clave])
                
                elif tipo_dato.lower() == "entero":

                    heroe[clave] = sanitizar_entero(heroe[clave])

                else:
                    #flotante
                    heroe[clave] = sanitizar_flotante(heroe[clave])
                

                valor_retorno = True
            
            else:

                valor_retorno = "Tipo de dato no reconocido"

        else:

            valor_retorno = "La clave especificada no existe en el heroe"

    else:

        valor_retorno = "Tipo de dato no reconocido"

    return valor_retorno


""" 3.5. Crear la función 'stark_normalizar_datos" la cual recibirá como parámetros:
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

        lista_claves = ["altura","peso","color_ojos","color_pelo","fuerza","inteligencia"]

        lista_tipo_dato = ["flotante","flotante","string","string","entero","string"]


        for elemento in lista_heroes:

            for key,dato in zip(lista_claves,lista_tipo_dato):

                sanitizar_dato(elemento,key,dato)
        
        print("Datos normalizados")

    else:

        print("Error: Lista de heroes vacia")


""" 4.1. Crear la función "generar_indice_nombres" la cual recibirá como parámetro:
● lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y generar una lista donde cada
elemento es cada palabra que componen el nombre de los personajes.

Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
["Howard", "the", "Duck", "Rocket", "Raccoon", "Wolverine", ... ]
La función deberá validar que:
● La lista contenga al menos un elemento
● Todos los elementos de lista_heroes sean del tipo diccionario
● Todos los elementos contengan la clave "nombre"
En caso de encontrar algún error, informar por pantalla: "El origen de datos no
contiene el formato correcto" """

def generar_indice_nombres(lista_heroes:list):

    if len(lista_heroes) > 0:

        lista_nombres_separados = []

        for elemento in lista_heroes:

            if "nombre" in elemento and type(elemento) == dict:

                nombre = elemento['nombre']

                nombre = re.sub('^\s+|\s+$',"",nombre)

                nombre = re.sub('-'," ",nombre)

                nombre = re.split(" ", nombre)

                if nombre != "":

                    lista_nombres_separados.extend(nombre)
            
            else:

                print("El origen de datos no contiene el formato correcto")

    else:

        print("El origen de datos no contiene el formato correcto")

        
    return lista_nombres_separados



""" 4.2. Crear la función "stark_imprimir_indice_nombre" la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá mostrar por pantalla el índice generado por la función
generar_indice_nombres con todos los nombres separados con un guión.
Por ejemplo:
Howard-the-duck-Rocket-Raccoon-Wolverine... """

def stark_imprimir_indice_nombre(lista_heroes:list):

    nombres_separados_guion = ""

    lista_indice_nombre = generar_indice_nombres(lista_heroes)

    for elemento in lista_indice_nombre:

        nombres_separados_guion += elemento + "-"
    
    print(nombres_separados_guion)


""" 5.1. Crear la función "convertir_cm_a_mtrs" la cual recibirá como parámetro:
● valor_cm: Un número que representa una medida en centímetros
La función deberá retornar el número recibido, pero convertido a la unidad
metros. La función deberá validar que el número recibido sea un número
flotante positivo, en caso de no serlo retornar -1 """

def convertir_cm_a_mtrs(valor_cm:float):

    if type(valor_cm) == float and re.search('^\d+\.\d+$',str(valor_cm)):

        pasaje_a_metros = valor_cm / 100

        valor_retorno = pasaje_a_metros

    else:

        valor_retorno = -1
    

    return valor_retorno


""" 5.2. Crear la función "generar_separador" la cual recibirá como parámetro
● patron: un carácter que se utilizará como patrón para generar el
separador
● largo: un número que representa la cantidad de caracteres que va
ocupar el separador.
● imprimir: un parámetro opcional del tipo booleano (por default definir
en True)
La función deberá generar un string que contenga el patrón especificado
repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
al otro, sin salto de línea)
Si el parámetro booleano recibido se encuentra en False se deberá solo
retornar el separador generado. Si se encuentra en True antes de retornarlo,
imprimirlo por pantalla
La función deberá validar:
● Que el parámetro patrón tenga al menos un carácter y como máximo
dos
● Que el parámetro largo sea un entero entre 1 y 235 inclusive
En caso de no verificarse las validaciones devolver "N/A"
Ejemplo de llamada:
generar_separador("*", 10)
Ejemplo de salida:
********** """

def generar_separador(patron:str,largo:int,imprimir=True):

    """ 
    ● patron: un carácter que se utilizará como patrón para generar el
    separador
    ● largo: un número que representa la cantidad de caracteres que va
    ocupar el separador.
    ● imprimir: un parámetro opcional del tipo booleano (por default definir
    en True) 
    """

    #valido que minimo debe haber un caracter y maximo 2 osea puede o no haber el segundo
    if re.search('^.{1}.?$', patron) and largo > 0 and largo < 236:

        patron_repetido = ""

        #pregunto si contiene cualquier caracter pero uno solo
        if re.search('^.$',patron):

            for elemento in range(largo):

                patron_repetido += patron

        else:
            #si ingresa es que hay dos, ya que antes valide que no haya mas de dos
            largo_para_dos_caracteres = largo / 2

            largo_para_dos_caracteres = int(largo_para_dos_caracteres)

            for elemento in range(largo_para_dos_caracteres):

                patron_repetido += patron

        #imprime el separador si coloca true o no coloca nada
        if imprimir == True:

            print(patron_repetido)

        valor_retorno = patron_repetido

    else:

        valor_retorno = "N/A"

    
    return valor_retorno


""" 5.3. Crear la función "generar_encabezado" la cual recibirá como parámetro

● titulo: un string que representa el título de una sección de la ficha
La función deberá devolver un string que contenga el título envuelto entre dos
separadores (estimar el largo requerido para tu pantalla).
Ejemplo de salida:
********************************************************************************
PRINCIPAL
********************************************************************************
La función deberá convertir el titulo recibido en todas letras mayúsculas """

def generar_encabezado(titulo:str):

    if type(titulo) == str:

        separadores = generar_separador("*",100,False)

        titulo = titulo.upper()

        titulo_envuelto = (separadores + '\n'
            + titulo + '\n'
            + separadores + '\n'
        )

        return titulo_envuelto

""" 5.4. Crear la función "imprimir_ficha_heroe" la cual recibirá como parámetro:
● heroe: un diccionario con los datos del héroe
La función deberá a partir los datos del héroe generar un string con el
siguiente formato e imprimirlo por pantalla::
***************************************************************************************
PRINCIPAL
***************************************************************************************
NOMBRE DEL HÉROE: Spider-Man (S.M.)
IDENTIDAD SECRETA: Peter Parker
CONSULTORA: Marvel Comics
CÓDIGO DE HÉROE : M-00000001
***************************************************************************************
FISICO
***************************************************************************************

ALTURA: 1,78 Mtrs.
PESO: 74,25 Kg.
FUERZA: 55 N
***************************************************************************************
SEÑAS PARTICULARES
***************************************************************************************
COLOR DE OJOS: Hazel
COLOR DE PELO: Brown """

def imprimir_ficha_heroe(heroe:dict):

    if type(heroe) == dict:

        titulo_principal = generar_encabezado("principal")

        titulo_fisico = generar_encabezado("fisico")

        titulo_particulares = generar_encabezado("señas particulares")

        print(titulo_principal + 
            "NOMBRE DEL HEROE: "+ heroe['nombre'] + ' ('+heroe['iniciales'] + ')\n'
            "IDENTIDAD SECRETA: "+ heroe['identidad'] + '\n'
            "NOMBRE DEL HEROE: "+ heroe['empresa'] + '\n'
            "NOMBRE DEL HEROE: "+ str(heroe['codigo_heroe']) + '\n'
            +titulo_fisico+ 
            "ALTURA: "+ str(heroe['altura']) + ' Mtrs\n'
            "PESO: "+ str(heroe['peso']) + ' Kg\n'
            "FUERZA: "+ str(heroe['fuerza']) + ' N\n'
            +titulo_particulares+ 
            "COLOR DE OJOS: "+ heroe['color_ojos'] + '\n'
            "COLOR DE PELO: "+ heroe['color_pelo'] + '\n'
        )





""" 5.5. Crear la función 'stark_navegar_fichas' la cual recibirá como parámetros:
● lista_heroes: la listas personajes
La función deberá comenzar imprimiendo la ficha del primer personaje de la
lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
● Si el usuario ingresa "1": se debe mostrar el héroe que se encuentra en
la posición anterior en la lista (en caso de estar en el primero, ir al
último)

● Si el usuario ingresa "2": se debe mostrar el héroe que se encuentra en
la posición siguiente en la lista (en caso de estar en el último, ir al
primero)

● Si ingresa "S": volver al menú principal

● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
ingrese un valor válido """

def stark_navegar_fichas(lista_heroes:list):

    if type(lista_heroes) == list:

        """ MOTIVO DE ALGUNAS COSAS
         
        La cantidad de heroes la paso tambien a una variables en negativo para luego comparar, por ejemplo hay 23 heroes y si le doy para atras tiene que ser
        en negativo, si llega hasta -22 quiere decir que llego al ultimo heroe en su posicion entonces tengo que comparlo y si llego restauro su posicion a 0 o -1,
        depende lo que solicita el ejercicio o lo que yo quiera
          
           
            
        """
        cantidad_heroes_positivos = len(lista_heroes)

        cantidad_heroes_negativo = cantidad_heroes_positivos * -1

        posicion = 0

        imprimir_ficha_heroe(lista_heroes[posicion])

        while True:

            dato_ingresado = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir")
            
            #valido
            while dato_ingresado != "1" and dato_ingresado != "2" and dato_ingresado != "S":

                dato_ingresado = input("ERROR [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir ")

            if dato_ingresado == "1":

                posicion += -1
            
            elif dato_ingresado == "2":

                posicion += 1 
            
            else:

                #salir
                break


            if posicion > cantidad_heroes_negativo and posicion < cantidad_heroes_positivos:

                imprimir_ficha_heroe(lista_heroes[posicion])

            #posicion positiva
            elif posicion == cantidad_heroes_positivos:

                posicion = 0

                imprimir_ficha_heroe(lista_heroes[posicion])

            else:
                #posicion negativa
                posicion = -1

                imprimir_ficha_heroe(lista_heroes[posicion])


#lo uso para incializar 
""" agregar_iniciales_nombre(lista_personajes)
stark_generar_codigos_heroes(lista_personajes) """


""" 6.1. Crear la función "imprimir_menu" que imprima las siguientes opciones por
pantalla:


1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir

____________________________________________________________
"""

def imprimir_menu():

    patron_separador = "-" * 100

    print('"""\n'
        '1 - Imprimir la lista de nombres junto con sus iniciales\n'
        '2 - Generar códigos de héroes\n'
        '\n'
        '3 - Normalizar datos\n'
        '4 - Imprimir índice de nombres\n'
        '5 - Navegar fichas\n'
        'S - Salir\n'
        '\n'+
        patron_separador+'\n'
          '"""')
    
""" 6.2. Crear la función 'stark_menu_principal'. No recibe parámetros.
La función deberá imprimir el menú de opciones y le pedirá al usuario que
ingrese una.
La función deberá retornar la respuesta del usuario """

def stark_menu_principal():

    imprimir_menu()

    opcion = input("Ingrese una opcion: ")

    return opcion

""" 6.3. Crear la función "stark_marvel_app_3" la cual recibirá como parámetro:
● lista_heroes: la lista de personajes
La función se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera (match solo para los que cuentan con
python 3.10+).
Debe informar por consola en caso de seleccionar una opción incorrecta y
volver a pedir el dato al usuario.
Reutilizar las funciones con prefijo "stark" donde crea correspondiente. """

#MUESTRA UN MENU CON TODAS LAS OPCIONES Y UTILIZA TODAS LAS FUNCIONES ANTERIORES
def stark_marvel_app_3(lista_heroes:list):


    #ACORDATE QUE CON TODAS ESTAS FUNCIONES AGREGAS, LAS INICIALES, EL NUMERO DE CODIGO
    agregar_iniciales_nombre(lista_heroes)

    cantidad_heroes = len(lista_heroes)

    for genero_codigo in range(cantidad_heroes):

        agregar_codigo_heroe(lista_heroes[genero_codigo],genero_codigo)

    #llamo el menu principal
    flag = True
    
    while flag == True:

        opcion_ingresada = stark_menu_principal()

        while opcion_ingresada != "1" and opcion_ingresada != "2" and opcion_ingresada != "3" and opcion_ingresada != "4" and opcion_ingresada != "5" and opcion_ingresada != "S":

            opcion_ingresada = stark_menu_principal()
        

        #1 - Imprimir la lista de nombres junto con sus iniciales
        if opcion_ingresada == "1":

            stark_imprimir_nombres_con_iniciales(lista_heroes)
        
        #2 - Generar códigos de héroes
        elif opcion_ingresada == "2":

            stark_generar_codigos_heroes(lista_personajes)
        
        #3 - Normalizar datos
        elif opcion_ingresada == "3":

            stark_normalizar_datos(lista_heroes)
        
        #4 - Imprimir índice de nombres
        elif opcion_ingresada == "4":

            stark_imprimir_indice_nombre(lista_heroes)
        
        #5 - Navegar fichas
        elif opcion_ingresada == "5":

            stark_navegar_fichas(lista_heroes)
        
        else:
            #salir
            break

stark_marvel_app_3(lista_personajes)