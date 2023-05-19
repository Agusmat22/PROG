import re 
#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS
""" 1.Contar letras: Crea una función que tome una cadena
de texto como argumento y
cuente el número de letras que contiene.
2.Eliminar caracteres: Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.
3.Contar palabras: Crea una función que tome una
cadena de texto como argumento y
cuente el número de palabras que contiene.
Suponga que las palabras están separadas por un
espacio.
4.Reemplazar palabras: Crea una función que tome una
cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.
5.Buscar patrón: Crea una función que tome dos cadenas
de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias
del patrón en la cadena principal y devolver una lista con
las posiciones donde se encontró el patrón. """

#1
#Cuenta la cantidad de caracteres de una variable
def contar_letrar(dato:str) -> int:

    dato = dato.strip()

    valor = None

    dato = re.sub(r'[^a-z-A-Z]','', dato)

    if dato.isalpha() == True:

        valor = len(dato)

    return valor

#2
def eliminar_caracteres(texto:str,caracter:str):

    texto_caracter_eliminado = texto.replace(f'{caracter} ','')

    return texto_caracter_eliminado

#3
def contar_palabras(texto:str) ->int:

    texto = texto.strip()

    palabras_en_lista = texto.split(" ")

    contador_palabras = 0

    for palabra in palabras_en_lista:

        if palabra != "":

            contador_palabras += 1

    return contador_palabras

    
#4
def reemplazar_caracteres(texto:str,palabra_reemplazada:str,reemplazo:str):

    texto = texto.strip()

    texto_reemplazado = texto.replace(palabra_reemplazada.lower(),reemplazo.lower())

    return texto_reemplazado

#5
""" 5.Buscar patrón: Crea una función que tome dos cadenas
de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias
del patrón en la cadena principal y devolver una lista con
las posiciones donde se encontró el patrón. """

def buscar_patron(cadena:str, patron:str):

    posiciones = []

    posiciones_encontradas = re.finditer(patron, cadena)

    for elemento in posiciones_encontradas:

        posiciones.append(elemento.start())

    return posiciones

buscar_patron("hola tengo hola y soy hola y hola y hola","hola")