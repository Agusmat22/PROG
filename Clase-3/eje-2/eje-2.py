#NOMBRE: Garcia Navas Agustin Matias

#TOMO LOS DATOS DEL ARCHIVO DATA_STARK
from data_stark import lista_personajes

""" 
1) Analizar detenidamente el set de datos
2) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
3) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
4) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
5) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
6) Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
7) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
8) Calcular e informar cual es el superhéroe más y menos pesado.
9) Ordenar el código implementando una función para cada uno de los valores informados.(HACER UNA OPCION DE CON LETRAS )
10) Construir un menú que permita elegir qué dato obtener 
"""


#2) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

""" Funcion que muestra los nombres del las listas """
def mostrar_nombres():
    for nombres in lista_personajes:

        print("\nNombre:",nombres["nombre"])

#3) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

""" Funcion que muestra la altura junto con el nombre """
def mostrar_altura_nombre():
    for altura in lista_personajes:

        print("\nNombre:",altura["nombre"],"| Altura:",altura["altura"])

#4) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

""" Funcion muestra el superheroe mas alto """
def superheroe_altura_max():

    flag = True

    heroe_max_altura = None

    nombre_heroe_max_altura = None

    for altura_maxima in lista_personajes:

        #la altura estaba como string y con float lo pasamos a entero con decimal osea float (flotante)
        if flag == True or float(altura_maxima["altura"]) > heroe_max_altura:

            heroe_max_altura = float(altura_maxima["altura"])

            flag = False
        
        

    print("\nEl superheroe mas alto mide:", heroe_max_altura)


#5) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

""" Funcion muestra el superheroe mas bajo """
def superheroe_altura_min():

    flag = True

    heroe_min_altura = None

    nombre_heroe_min_altura = None

    for altura_minima in lista_personajes:

        #la altura estaba como string y con float lo pasamos a entero con decimal osea float (flotante)
        if flag == True or float(altura_minima["altura"]) < heroe_min_altura:

            heroe_min_altura = float(altura_minima["altura"])

            nombre_heroe_min_altura = altura_minima["nombre"]

            flag = False
        
        

    print("\nEl superheroe mas bajo mide:", heroe_min_altura)




#6) Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)

""" Esta funcion muestra el promedio de las alturas """
def promedio_altura():

    acum_alturas = 0

    cont = 0

    for acumulador_altura in lista_personajes:

        acum_alturas += float(acumulador_altura["altura"])
        cont += 1

    promedio_altura = acum_alturas / cont

    print("\nPromedio altura:",promedio_altura)

#7) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

def nombre_altura_max_min():

    #var altura max
    flag = True
    heroe_max_altura = None
    nombre_heroe_max_altura = None

    #var altura min

    heroe_min_altura = None
    nombre_heroe_min_altura = None


    for altura_max_min in lista_personajes:

        #la altura estaba como string y con float lo pasamos a entero con decimal osea float (flotante)
        if flag == True:

            heroe_max_altura = float(altura_max_min["altura"])

            nombre_heroe_max_altura = altura_max_min["nombre"]

            heroe_min_altura = float(altura_max_min["altura"])

            nombre_heroe_min_altura = altura_max_min["nombre"]
            flag = False
        
        elif float(altura_max_min["altura"]) > heroe_max_altura:

            heroe_max_altura = float(altura_max_min["altura"])

            nombre_heroe_max_altura = altura_max_min["nombre"]
        
        elif float(altura_max_min["altura"]) < heroe_min_altura:

            heroe_min_altura = float(altura_max_min["altura"])

            nombre_heroe_min_altura = altura_max_min["nombre"]


    print("\nAltura MINIMA\nNombre:",nombre_heroe_min_altura,"\nAltura MAXIMA\nNombre:",nombre_heroe_max_altura)

#8) Calcular e informar cual es el superhéroe más y menos pesado.

""" Esta funcion muestra los pesos maximos y minimos """
def mostrar_pesos_min_max():
    flag = True
    superheroe_peso_max = None
    nombre_peso_max = None
    nombre_peso_min = None
    superheroe_peso_min = None


    for peso_max_min in lista_personajes:

        if flag == True:

            flag = True
            superheroe_peso_max = float(peso_max_min["peso"])
            nombre_peso_max = peso_max_min["nombre"]
            superheroe_peso_min = float(peso_max_min["peso"])
            nombre_peso_min = peso_max_min["nombre"]
            flag = False
        
        elif float(peso_max_min["peso"]) > superheroe_peso_max:

            superheroe_peso_max = float(peso_max_min["peso"])
            nombre_peso_max = peso_max_min["nombre"]

        elif float(peso_max_min["peso"]) < superheroe_peso_min:

            superheroe_peso_min = float(peso_max_min["peso"])
            nombre_peso_min = peso_max_min["nombre"]

    print("\nSuperheroe mas delgado es:\nNombre:",nombre_peso_min,"\nSuperheroe mas pesado es:\nNombre:",nombre_peso_max)



#10) Construir un menú que permita elegir qué dato obtener 

""" Esta funcion muestra un menu con varias opciones para seleccionar """
def menu_opciones():

    print("\nBienvenidos a Marvel\n"
        "\n" 
            "A) Mostrar nombre de cada Superheroe\n"
            "B) Mostrar nombre y altura de cada Superheroe\n"
            "C) Mostrar la altura del Superheroe mas bajo\n"
            "D) Mostrar la altura del Superheroe mas alto\n"
            "E) Mostrar la altura promedio de los Superheroes\n"
            "F) Mostrar el nombre de los Superheroes mas alto y bajo\n"
            "G) Mostrar el mas pesado y liviano de los Superheroe\n" 
        "\n"
            "H) Salir\n"
        )

    opcion = input("\nIngrese una letra de la (A-H) para seleccionar un apartado: ")
    opcion = opcion.upper()

    return opcion





continuar = True

while continuar == True :

    #llamo a la funcion menu y guardo el dato ingresado por opcion en otra variable

    opcion_elegida = menu_opciones()

    if opcion_elegida == "A":

        mostrar_nombres()

    elif opcion_elegida == "B":

        mostrar_altura_nombre()
    
    elif opcion_elegida == "C":

        superheroe_altura_min()
    
    elif opcion_elegida == "D":

        superheroe_altura_max()
    
    elif opcion_elegida == "E":

        promedio_altura()
    
    elif opcion_elegida == "F":

        nombre_altura_max_min()
    
    elif opcion_elegida == "G":

        mostrar_pesos_min_max() 

    else:

        print("Selecciono 'salir', Gracias por utilizar nuestro programa")
        break 
































    