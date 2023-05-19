#importo las listas
from data_stark import lista_personajes

#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS


#EJERCICIO 1

""" 1.1) Crear la función "extraer_iniciales"que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)
● En el caso que el nombre del personaje contenga el artículo "the" se
deberá omitir de las iniciales
● Se deberá verificar si el nombre contiene un guión " - "y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
● Que el string recibido no se encuentre vacío
Devolver "N/A" en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D. """

#esta funcion extrae las iniciales del nombre
def extraer_iniciales(nombre_heroe:str):

    if nombre_heroe == "":

        return "N/A"
    
    #paso la palabra a texto
    iniciales = nombre_heroe.upper()

    #pregunto si "the" se encuentra en iniciales, de ser asi lo reemplazo
    if "THE" in iniciales :

        iniciales = iniciales.replace("THE","")
    
    #en caso que hay guion lo reemplazo en espacio en blanco
    if "-" in iniciales:

        iniciales = iniciales.replace("-"," ")

    #elimino todo los espacios en blanco al principio y final
    iniciales = iniciales.strip()

    #divido los nombres en lista donde estan los espacios en blanco los convierto en lista para que contengan coma y luego poder recorrerlo con un for
    iniciales = iniciales.split(" ")


    #variable con str vacio ya que luego se va concatenar el resultado
    resultado = ""
    
    for elementos in iniciales:
        #pregunto si elementos es distinto de espacios vacios ya que si hay espacios entre juan y calor van a ingresar en el mensaje como "", de este modo los descarto
        if elementos != "":
            #agrego el valor del indice 0 de la palabra junto a un punto y lo guardo en mi variable, en caso que haya dos o tres nombres se repetira
            resultado += elementos[0] + "." 

    
    return(resultado)


""" 1.2. Crear la función "definir_iniciales_nombre" la cual recibirá como
parámetro:
● heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar "iniciales" y su valor será el obtenido de
llamar a la función "extraer_iniciales"
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave "nombre"
En caso de encontrar algún error retornar False, caso contrario retornar True """


#esta funcion muestra una clave nueva a un diccionario con las iniciales del nombre y retorna true o false si hay algun error en el diccionario
def definir_iniciales_nombre(heroe:dict):

    #heroe es distinto a un diccionario o 'nombre' no estan en heroe, retorno n/a
    if type(heroe) != dict or 'nombre' not in heroe:

        return False
    
    #creo una clave 'iniciales' y le indico su valor. llamo a la funcion anterior y le indico la clave que deseo que utilice
    heroe['iniciales'] = extraer_iniciales(heroe['nombre'])

    return True


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

#esta funcion itera la lista pasandole a cada heroe la funcion definir_iniciales_nombre
def agregar_iniciales_nombre(lista_heroes:list):

    #pregunto si el tipo es distinto a una lista o si hay menos de un elemento. Len cuenta la cantidad de elementos
    if type(lista_heroes) != list or len(lista_heroes) < 1:

        return False

    flag = True

    for heroes in lista_heroes:


        if definir_iniciales_nombre(heroes) == False:

            print("El origen de datos no contiene el formato correcto")
            
            flag = False

            break
        else: 

            definir_iniciales_nombre(heroes)
    
    if flag == False:

        #devuelve este valor si fue un fracaso
        return False
    
    else:

        #devuelve este valor si se realizo con exito
        return True


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
…
La función no retorna nada """

#esta funcion muestra por pantalla el nombre y al lado las iniciales con su nombre del diccionario
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    #valido
    if type(lista_heroes) != list or len(lista_heroes) < 1:

        return False

    agregar_iniciales_nombre(lista_heroes)

    for heroe in lista_heroes:

        print('* ',heroe['nombre'],'(',heroe['iniciales'],')')
""" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- """

#EJERCICIO 2

""" 2.1. Crear la función "generar_codigo_heroe" la cual recibirá como
parámetros:
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
● genero_heroe: un string que representa el género del héroe ( puede
tomar los valores "M", "F" o "NB")
La función deberá generar un string con el siguiente formato:

GENERO-000…000ID
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

#esta funcion crea un codigo en base al numero ingresado y el genero, con un maximo de 10 caracteres
def generar_codigo_heroe(id_heroe:int,genero:str):

    #el genero lo combierto a mayuscula
    genero = genero.upper()

    #valido las opciones y los tipos
    if type(id_heroe) != int or type(genero) != str or genero != "M" and genero != "F" and genero != "NB":

        return "N/A" 
    
    #paso a str el numero para poder trabajarlo con metodos y poder valir que no sea mayor a 8 caracteres ingresado
    id_heroe = str(id_heroe)

    #valido si el numero ingresado tiene mas de 8 caracteres
    if len(id_heroe) > 7:

        return "N/A"
    

    #consulto si es nb para agregarle un cero menos ya que tiene un caracter mas
    if genero == "nb":

        numero_ceros_agregados = id_heroe.zfill(7)

    else:

        numero_ceros_agregados = id_heroe.zfill(8)

    #concateno los valores y le agrego el '-'
    codigo_genero_numeros = f'{genero}-{numero_ceros_agregados}'


    #retorno el valor
    return codigo_genero_numeros

""" 2.2. Crear la función "agregar_codigo_heroe" la cual recibirá como
parámetro:
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

    if type(heroe) != dict or type(id_heroe) != int:

        return False


    heroe['codigo_heroe'] = generar_codigo_heroe(id_heroe,heroe['genero']) 


    return heroe

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

    #corroboro con len si hay mas de un elemento en la lista
    if len(lista_heroes) < 1 or type(lista_heroes) != list:

        return  "El origen de datos no contiene el formato correcto"
    
    #recorro con un for si dentro de la lista el tipo son diccionarios
    for lista_corroborar in lista_heroes:

        if type(lista_corroborar) != dict:

            return  "El origen de datos no contiene el formato correcto"
    
    #con len cuento cuantos diccionarios hay y me da el numero de superheroes totales
    cantidad_superheroes = len(lista_heroes)

    #recorro la cantidad de superheroes con range y por cada iteracion le agrego el codigo en el diccionario
    for generar_codigo in range(cantidad_superheroes):

        #generar_codigo es para que vaya sumando el numero en el codigo en cada iteracion
        agregar_codigo_heroe(lista_heroes[generar_codigo], generar_codigo)

    
    print(f'**Se asignaron {cantidad_superheroes} codigos**\n')
    
    #recorro de nuevo la cantidad de superheroes y segun su posicion muestro el codigo de cada uno
    for indice in range(cantidad_superheroes):

        print('* El heroe N*:',indice,'su numero de codigo es:',lista_heroes[indice]['codigo_heroe'])




""" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- """

#EJERCICIO 3

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

#Analiza un str si es un numero entero y lo convierte
def sanitizar_entero(numero_str:str):

    if type(numero_str) == str:

        numero_str = numero_str.strip()
        numero_str = numero_str.replace(" ","")

        if numero_str[0] == "-":

            #isdigit() corrobora si el string es exclusivamente numerico desde la posicion 1 en adelante en caso que no sea devolvera false
            #coloco desde la posicion 1: ya que antes consulte si en la posicion 0 estaba el simbolo '-'
            if numero_str[1:].isdigit() == False:

                return -1
            else:
                #si es negativo retorna
                return -2
        
        #si en la posicion [0] no hay un simbolo negativo pregunto si toda la cadena es numerica
        elif numero_str.isdigit() == False:

            return -1

        numero_str = int(numero_str)

        #retorno el numero ingresado
        return numero_str
    
    else:

        return -3
    
    
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

#analiza si el string es un numero flotante positivo y lo devuelve en flotante
def sanitizar_flotante(numero_str: str):
    
    #valido el tipo de variable
    if type(numero_str) != str:

        return -3
    
    #pregunto si hay un solo '.' en la cadena
    elif numero_str.count(".") == 1:
        
        #reemplazando el '.' y el '-', consulto si de la cadena son numeros
        if numero_str.replace(".","").replace("-","").isdigit() == False:

            return -1
        
        else:

            #pregunto si el primer caracter inicia con '-'
            if numero_str[0] == "-":

                return(-2)
            
            else:
                #convierto la cadena en flotante
                numero_flotante = float(numero_str)

                return numero_flotante
    
    else:

        return -3



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

#analiza si el dato es solo alfabetico y lo retorna en minuscula
def sanitizar_string(valor_str:str,valor_por_defecto:str):

    #valido si '/' se encuentra en la cadena
    if "/" in valor_str:

        valor_str = valor_str.replace("/"," ")

    #consulto sacando los espacios vacios el resto es una cadena alfabetica
    if valor_str.replace(" ","").isalpha() == True:

        valor_str = valor_str.lower()

        return valor_str
    
    #consulto si el valor es una cadena vacia
    elif valor_str == "":
        
        valor_por_defecto = valor_por_defecto.lower()

        return valor_por_defecto
    
    else:

        return "N/A"

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

#funcion que se ocupa se sanitizar una lista con diccionarios y por parametros le pasamos el diccionario, la key que buscamos dentro del mismo y el tipo de dato que se encuentra dentro de la key, en caso de sanitizar retorna true y en el contrario false
def sanitizar_dato(heroe,clave,tipo_dato):

    #valido el tipo str
    if type(tipo_dato) == str:

        #el tipo de dato y clave lo sanitizo para corroborar que es un texto con mi funcion anterior
        sanitizar_string(tipo_dato,tipo_dato)

        sanitizar_string(clave,clave)

        #pregunto si el parametro clave se encuentra dentro del diccionario
        if clave in heroe:

            #pregunto segun el tipo de dato es la funcion que va sanitizar
            if tipo_dato == "string":

                sanitizar_string(heroe[clave],heroe[clave])

                return True

            elif tipo_dato == "entero":

                sanitizar_entero(heroe[clave]) 

                return True
            
            elif tipo_dato == "flotante":

                sanitizar_flotante(heroe[clave])

                return True
            
            else:
                
                return False
            
        else:

            print("La clave especificada no existe en el heroe")

    else:    

        print("Tipo de dato no reconocido")
    

""" 3.5. Crear la función " stark_normalizar_datos" la cual recibirá como
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

#esta funcion recorre la lista con diccionarios dentro y utiliza la funcion 'sanitizar_dato' para sanitizar todos los datos que contiene cada dict, luego imprime Datos normalizados 
def stark_normalizar_datos(lista_heroes):

    #valido que no ingrese una lista vacia, consultando con len cuanto elemento hay dentro de la misma
    if len(lista_heroes) == 0:

        print("ERROR: Lista de heroes vacia")

    #las claves que deben corroborarse
    lista_claves = ["altura", "peso", "color_ojos", "color_pelo", "fuerza" ,"inteligencia"]

    #cree yo el tipo de dato para sus respectivas claves
    lista_tipo_dato = ["flotante","flotante","string","string","entero","string"]

    #inicializo variable
    sanitizar = ""

    #itera cada diccionario
    for heroes in lista_heroes:

        #en cada iteraccion del diccionario itero las listas para que sanitize todas las claves mencionada por cada superheroe
        for clave, dato in zip(lista_claves,lista_tipo_dato):

            sanitizar = sanitizar_dato(heroes,clave,dato)


    #si me devuelve true es que fue sanitizado
    if sanitizar == True:

        print("Datos normalizados")

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

#retorna todos los nombres por partes en una lista 
def generar_indice_nombres(lista_heroes:list):
    
    #creo la lista vacia para luego pasarle las partes de los nombres
    lista_nueva = []

    #validado si contiene mas de un elemento
    if len(lista_heroes) > 0:

        #itero cada elemento(dict) de la lista
        for elementos in lista_heroes:

            #pregunto si el tipo es distinto a dict o si la key 'nombre' no se encuentra en elementos
            if type(elementos) != dict or "nombre" not in elementos:

                print("El origen de datos no contiene el formato correcto")

            else:

                #quito los espacios vacios al principio y final
                elementos['nombre'] = elementos['nombre'].strip()

                #pregunto si se encuentra '-' en el diccionario
                if '-' in elementos['nombre']:
                    elementos['nombre'] = elementos['nombre'].replace("-"," ")  #reemplazo el - por un espacio vacio

                if "/" in elementos['nombre']:
                    elementos['nombre'] = elementos['nombre'].replace("/"," ") #reemplazo el / por un espacio vacio

                elementos['nombre'] = elementos['nombre'].split(" ") #Convierto los espacios en ',' para que se vuelvan en listas los nombres(se divide por partes)

                
                #pregunto si el elemento es distino a una cadena vacia
                if elementos['nombre'] != "":
                    
                    #agrego todos las partes de los nombres con .extend() a una lista nueva 
                    lista_nueva.extend(elementos['nombre'])
                    
    print(lista_nueva)
      
    return lista_nueva

generar_indice_nombres(lista_personajes)

""" 4.2. Crear la función "stark_imprimir_indice_nombre" la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá mostrar por pantalla el índice generado por la función
generar_indice_nombres con todos los nombres separados con un guión.
Por ejemplo:
Howard-the-duck-Rocket-Raccoon-Wolverine… """

#imprime la los nombres con (-)de los personajes utilizando la funcion anterior
def stark_imprimir_indice_nombre(lista_heroes:list):

    lista_nombres = generar_indice_nombres(lista_heroes)

    if type(lista_nombres) == list:
        elemento = ""

        for nombre in lista_nombres:

            elemento += nombre + "-"
        
        
        print(elemento)


""" 5.1. Crear la función "convertir_cm_a_mtrs" la cual recibirá como parámetro:
● valor_cm: Un número que representa una medida en centímetros
La función deberá retornar el número recibido, pero convertido a la unidad
metros. La función deberá validar que el número recibido sea un número
flotante positivo, en caso de no serlo retornar -1 """

#esta funcion convierte un flotante en centimetros positivo a metros y lo retorna. Si el flotante es negativo retorna -1
def convertir_cm_a_mtrs(valor_cm:float):

    #valido el tipo
    if type(valor_cm) == float:

        if valor_cm >= 0.1:

            #pasaje de centimetros a metro
            pasaje_cm_a_mtrs = valor_cm / 100

            return pasaje_cm_a_mtrs
        
        else:

            return -1


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
**********                """

#patron puede ser(*,/,+,etc)


#retorna e imprime la cantidad de patrones que se ingresan como parametro  (algunos numero impar imprime uno menos PREGUNTAR AL PROFE SI ESTA BIEN O NO)
def generar_separador(patron:str,largo:int,imprimir:True):

    #valido los tipos
    if type(patron) == str and type(largo) == int and type(imprimir) == bool:

        #valido la cantidad de caracteres y el minimo y maximo de largo
        if len(patron) > 0 and len(patron) < 3 and largo > 0 and largo < 236:


            patron_recibido = patron

            #cuento la cantidad de patrones que ingreso
            cantidad_patrones = len(patron_recibido)

            #creo esta variable para guardar el resultado
            resultado = ""

            #divido la cantidad de patrones por si llega a ingresar 2 y que imprima los que solicito
            cantidad_separadores_imprimir = largo / cantidad_patrones

            #paso a entero la cantidad de separadores a imprimir porque sino queda en float
            cantidad_separadores_imprimir = int(cantidad_separadores_imprimir)

            #recorro la cantidad de separadores a imprimir que paso como parametro
            for separador in range(cantidad_separadores_imprimir):

                resultado += patron_recibido

            #pregunto si desea imprimir o no segun el parametro que haya ingresado
            if imprimir == True:

                print(resultado)

                return resultado
            
            else:

                return resultado
                

        else:

            return "N/A"


""" 5.3. Crear la función "generar_encabezado" la cual recibirá como parámetro
● titulo: un string que representa el título de una sección de la ficha
La función deberá devolver un string que contenga el título envuelto entre dos
separadores (estimar el largo requerido para tu pantalla).
Ejemplo de salida:
********************************************************************************
PRINCIPAL
********************************************************************************
La función deberá convertir el titulo recibido en todas letras mayúsculas """

#retorna el titulo ingresao como parametro mas un separador que diferencia el titulo del resto
def generar_encabezado(titulo:str):

    if type(titulo) == str and len(titulo) > 0:

        titulo_ingresado = titulo.upper()

        separador = generar_separador("*",140,False)

        resultado = f'{separador}\n{titulo_ingresado} \n{separador}'

        return resultado


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

#genera un string mostrando la ficha del heroe y lo imprime
def imprimir_ficha_heroe(heroe:dict):

    #titulo principal
    titulo_principal = generar_encabezado("Principal")

    titulo_fisico = generar_encabezado("Fisico")

    titulo_particulares = generar_encabezado("Señas particulares")

    print(titulo_principal,'\n'
        
        'NOMBRE DEL HEROE:',heroe['nombre'],'('+ heroe['iniciales']+')','\n'
        'IDENTIDAD SECRETA:',heroe['identidad'],'\n'
        'CONSULTORA:',heroe['empresa'],'\n'
        'CODIGO DE HEROE:',heroe['codigo_heroe'],'\n' +
        titulo_fisico,'\n' +
        'ALTURA:',heroe['altura'],'Mtrs.\n'
        'PESO:',heroe['peso'],'Kg.\n'
        'FUERZA:',heroe['fuerza'],'N.\n'+
        titulo_particulares,'\n'+
        'COLOR DE OJOS',heroe['color_ojos'],'\n'
        'COLOR DE PELO',heroe['color_pelo']






    )




 

""" 5.5. Crear la función "stark_navegar_fichas" la cual recibirá como
parámetros:
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


#funcion imprime la ficha de los heroes con un menu para seleccionar cada uno para adelante y para atras
def stark_navegar_fichas(lista_heroes:list):

    #bandera para el while
    flag = True

    #el acumulador de numero para identificar la posicion segun lo ingresado por el boton
    boton_posicion = 0

    #guardo la cantidad de elementos dentro de la lista
    cantidad_heroes = len(lista_heroes)

    #guardo la cantidad de elementos dentro de la lista pero en numero negativo
    cantidad_heroes_negativo = cantidad_heroes * -1

    imprimir_ficha_heroe(lista_heroes[boton_posicion])

    while flag == True:

        
        boton = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir: ")

        while boton != "1" and boton != "2" and boton != "S":

            boton = input("ERROR, [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir: ")

        #consulto segun el valor ingresado
        if boton == "S":

            break
        
        elif boton == "1":

            boton_posicion += -1
        
        elif boton == "2":

            boton_posicion += 1

        #pregutno si el cont de boton es menor a la cantidad de elementos de la lista (heroes) o es mayor a la cantidad de elementos(heroes) de la lista negativa
        if boton_posicion < cantidad_heroes and boton_posicion > cantidad_heroes_negativo:

            imprimir_ficha_heroe(lista_heroes[boton_posicion])
        
        #si el contandor es igual al valor de elementos totales reseteo el boton y lo vuelvo a cero
        elif boton_posicion == cantidad_heroes:

            #lo resto ya que la cantidad de heroes es en positivo
            boton_posicion = boton_posicion - cantidad_heroes

            imprimir_ficha_heroe(lista_heroes[boton_posicion])
        
        #si el contandor es igual a la cantidad de heroes totales reseteo el boton y lo vuelvo a cero
        elif boton_posicion == cantidad_heroes_negativo:

            #lo sumo ya que la cantidad de heroes es en negativo
            boton_posicion = boton_posicion + cantidad_heroes

            imprimir_ficha_heroe(lista_heroes[boton_posicion])

""" 6.1. Crear la función "imprimir_menu" que imprima las siguientes opciones
por pantalla:
'''

1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes

3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir
____________________________________________________________
''' 
"""

#IMPRIME UN MENU PARA LAS FUNCIONES ANTERIORES
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



""" 6.2. Crear la función "stark_menu_principal". No recibe parámetros.
La función deberá imprimir el menú de opciones y le pedirá al usuario que
ingrese una.
La función deberá retornar la respuesta del usuario """

def stark_menu_principal():

    imprimir_menu()

    opcion = input('Ingrese una opcion: ')

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

#stark_marvel_app_3(lista_personajes)




