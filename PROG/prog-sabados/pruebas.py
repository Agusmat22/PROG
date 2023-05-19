import io
import re
from data_stark import lista_personajes

alumnos = [    {'nombre': 'Lucía', 'edad': 18, 'nota': 8},
               {'nombre': 'Pedro', 'edad': 19, 'nota': 7},    
               {'nombre': 'María', 'edad': 20, 'nota': 9},    
               {'nombre': 'Juan', 'edad': 19, 'nota': 6},    
               {'nombre': 'Ana', 'edad': 18, 'nota': 8},    
               {'nombre': 'Carlos', 'edad': 20, 'nota': 7},    
               {'nombre': 'Sofía', 'edad': 19, 'nota': 9},    
               {'nombre': 'Miguel', 'edad': 18, 'nota': 7},    
               {'nombre': 'Laura', 'edad': 20, 'nota': 8},    
               {'nombre': 'Diego', 'edad': 19, 'nota': 7},    
               {'nombre': 'Elena', 'edad': 18, 'nota': 9},    
               {'nombre': 'David', 'edad': 20, 'nota': 3},    
               {'nombre': 'Marcela', 'edad': 19, 'nota': 8},    
               {'nombre': 'Andrés', 'edad': 18, 'nota': 7},    
               {'nombre': 'Florencia', 'edad': 20, 'nota': 9}]


def valor_minimo(lista:list,tipo:str):

    if type(tipo) == str and len(lista) > 0:
        
        flag = True

        valor_minimo = None

        for i in lista:

            if flag == True:

                valor_minimo = i[tipo]
                flag = False
            
            elif valor_minimo > i[tipo]:

                valor_minimo = i[tipo]

        
    return valor_minimo

def valor_maximo(lista:list,tipo:str):

    if type(tipo) == str and len(lista) > 0:

        flag = True
        valor_maximo = None

        for alumno in lista:

            if flag == True:

                flag = False
                valor_maximo = alumno[tipo]

            elif valor_maximo < alumno[tipo]:

                valor_maximo = alumno[tipo]

        return valor_maximo

def sanitizar_numero(numero:str):

    if type(numero) == str:

        if re.search('^[0-9]+$',numero):

            numero = int(numero)
        
        elif re.search('^[0-9]+\.[0-9]+$',numero):

            numero = float(numero)

    

    return numero


def ordenar_lista(lista:list,tipo:str):

    flag = True

    while flag == True:

        flag = False

        for i in range(len(lista)-1):

            lista[i][tipo] = sanitizar_numero(lista[i][tipo])
            lista[i+1][tipo] = sanitizar_numero(lista[i+1][tipo])

            if lista[i][tipo] > lista[i+1][tipo]:

                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                flag = True

    return lista


            





def imprimir_listado_alumnos(lista:list):

    nota_minima = valor_minimo(lista,'nota')

    nota_maxima = valor_maximo(lista,'nota')

    lista_ordenada = ordenar_lista(lista,'nota')

    mensaje = ""

    for i in lista_ordenada:

        mensaje += 'Nombre: '+i['nombre']+', Edad: '+str(i['edad'])+', Nota: '+str(i['nota'])+'\n'

    print('" ALUMNMOS DE 6to B | TURNO TARDE | "\n'
          '\n'
          f'Nota maxima: {nota_maxima} \nNota minima: {nota_minima}\n\nLista de alumnos: \n{mensaje}'
          )


    return mensaje



def guardar_lista_en_archivo_csv(nombre_archivo:str,contenido:str):

    with open(f'prog-sabados\\{nombre_archivo}.csv','w', encoding='utf-8') as archivo:

        lista_para_csv = contenido.split('\n')

        for linea in lista_para_csv:

            mensaje = linea+'\n'
            archivo.write(mensaje)
            
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

import io

def guardar_archivo(nombre:str,contenido:str):

    with open(f'prog-sabados\\{nombre}.csv','w+') as archivo:

        archivo.write(contenido)
    
    if isinstance(archivo,io.TextIOWrapper):

        valor_retorno = True

        mensaje = f'Se creo el archivo: {nombre}.csv'

        print(mensaje)
    else:

        valor_retorno = False


    return valor_retorno





""" 1.6. Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula). """


def capitalizar_palabras(dato:str):

    if type(dato) == str and dato != '':

        dato = dato.strip()

        if re.search('^[a-z\)\(/\s?-]+$',dato,re.IGNORECASE):
            
            lista_palabras = dato.split(' ')

            palabra_capitalizada = ""

            for palabra in lista_palabras:

                palabra_capitalizada += palabra.capitalize() + " "
            
            dato = palabra_capitalizada[:-1]

    
    return dato

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

def obtener_lista_de_tipos(lista_heroes:list,key:str)->set:

    lista_variedad_tipos = []

    for heroe in lista_heroes:

        if key in heroe:

            lista_variedad_tipos.append(heroe[key].lower())
        
        else:
            lista_variedad_tipos.append('N/A')

    lista_variedad_tipos = set(lista_variedad_tipos)

    return lista_variedad_tipos


""" 6.2. Crear la función 'normalizar_dato' la cual recibirá por parámetro un
dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representará el valor por defecto a colocar
en caso de que el valor está vacío. Deberá validar que el dato no esté
vacío, en caso de estarlo lo reemplazará con el valor default pasado
por parámetro y lo retornará, caso contrario lo retornará sin
modificaciones. """

def normalizar_dato(dato:str,valor_por_defecto:str):

    if dato == "":

        dato = valor_por_defecto


    return dato


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

def normalizar_heroe(heroe:dict,key:str):

    if type(heroe) == dict and key !="":

        heroe[key] = capitalizar_palabras(heroe[key])

        heroe[key] = normalizar_dato(heroe[key],'N/A')

        heroe['nombre'] = capitalizar_palabras(heroe['nombre'])

    return heroe

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
} """

def obtener_heroes_por_tipo(lista_heroes:list,variedad_datos:set,key:str):

    diccionario_tipos = {}

    for dato in variedad_datos:

        lista_nombres = []

        for heroe in lista_heroes:

            if key in heroe:
                
                heroe[key] = normalizar_dato(heroe[key],'N/A')

                if heroe[key].lower() == dato:

                    lista_nombres.append(heroe['nombre'])



        diccionario_tipos[dato] = lista_nombres

    return diccionario_tipos







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

def guardar_heroes_por_tipo(heroe:dict,key:str):

    mensaje = ""

    for clave,valor in heroe.items():

        clave = capitalizar_palabras(clave)

        mensaje += key + ' '+ clave + ': '+ ' | '.join(valor) + '\n'
    
    print(mensaje)

    nombre_archivo = f'heroes_segun_{key}'

    valor = guardar_archivo(nombre_archivo,mensaje)

    return valor





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

def stark_listar_heroes_por_dato(lista_heroes:list,key:str):

    variedad = obtener_lista_de_tipos(lista_heroes,key)

    valor = obtener_heroes_por_tipo(lista_heroes,variedad,key)

    confirmacion = guardar_heroes_por_tipo(valor,key)

    return confirmacion

stark_listar_heroes_por_dato(lista_personajes,'color_ojos')