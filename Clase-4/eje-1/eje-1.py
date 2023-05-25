#IMPORTO LA LISTA
from data_stark import lista_personajes

#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS

""" Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú (genérico) que permita acceder a cada uno de los puntos por
separado. Cada uno de los puntos debe ser desarrollado en una función distinta.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de género
M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de género
F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con "No Tiene").
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia 
"""

#PARA VALIDAR SI FUNCIONA MIS FUNCIONES
""" lista_prueba = [
    {
        'genero' : 'M',
        'altura' : '150'
    },
    {
        'genero' : 'M',
        'altura' : '100'
    }
    
    ] """


#MENU GENERICO
def menu_generico(lista):

    for menu in lista:

        print(menu)

    opcion = input("Elija una opcion")

    return opcion

#A)RETORNA LOS NOMBRES DE LOS SUPERHEROES DE GENERO MASCULINO EN UNA LISTA, Y EN EL PARAMETRO INGRESAMOS LA LISTA QUE DESEAMOS
def obtener_superheroes_masculino(lista_generica):

    lista_nombres_m = []

    for genero_m in lista_generica:

        if genero_m['genero'] == 'M':

            lista_nombres_m.append(genero_m['nombre'])

    return lista_nombres_m

#B)RETORNA LOS NOMBRES DE LOS SUPERHEROES DE GENERO FEMENINO EN UNA LISTA, Y EN EL PARAMETRO INGRESAMOS LA LISTA QUE DESEAMOS
def obtener_superheroes_femenino(lista_generica):

    lista_nombres_f = []

    for genero_f in lista_generica:

        if genero_f['genero'] == 'F':

            lista_nombres_f.append(genero_f['nombre'])

    return lista_nombres_f

#C)RETORNA EL NOMBRE DE LA ALTURA MAXIMA DE LOS SUPERHEROES DEL GENERO MASCULINO
def obtener_superheroe_mas_alto_masculino(lista_generica):

    flag = True

    superheroe_altura_maxima = None

    nombre_superheroe_altura_max = None

    for superheroe_altura in lista_generica:

        if superheroe_altura['genero'] == 'M':

            if flag == True or float(superheroe_altura["altura"]) > superheroe_altura_maxima:

                superheroe_altura_maxima = float(superheroe_altura["altura"])

                nombre_superheroe_altura_max = superheroe_altura["nombre"]

                flag = False

    return nombre_superheroe_altura_max
         
#D)RETORNA EL NOMBRE DE LA ALTURA MAXIMA DE LOS SUPERHEROES DEL GENERO FEMENINO
def obtener_superheroe_mas_alto_femenino(lista_generica):

    flag = True

    superheroe_altura_maxima = None

    nombre_superheroe_altura_max = None

    for superheroe_altura in lista_generica:

        if superheroe_altura['genero'] == 'F':

            if flag == True or float(superheroe_altura["altura"]) > superheroe_altura_maxima:

                superheroe_altura_maxima = float(superheroe_altura["altura"])

                nombre_superheroe_altura_max = superheroe_altura["nombre"]

                flag = False

    return nombre_superheroe_altura_max

#E)RETORNA EL NOMBRE DEL SUPERHEROE CON ALTURA MINIMA DEL GENERO MASCULINO
def obtener_superheroe_mas_bajo_masculino(lista_generica):

    flag = True

    superheroe_altura_minima = None

    nombre_superheroe_altura_min = None

    for superheroe_altura in lista_generica:

        if superheroe_altura['genero'] == 'M':

            if flag == True or float(superheroe_altura["altura"]) < superheroe_altura_minima:

                superheroe_altura_minima = float(superheroe_altura["altura"])

                nombre_superheroe_altura_min = superheroe_altura["nombre"]

                flag = False

    return nombre_superheroe_altura_min

#F)RETORNA EL NOMBRE DEL SUPERHEROE CON ALTURA MINIMA DEL GENERO FEMENINO
def obtener_superheroe_mas_bajo_femenino(lista_generica):

    flag = True

    superheroe_altura_minima = None

    nombre_superheroe_altura_min = None

    for superheroe_altura in lista_generica:

        if superheroe_altura['genero'] == 'F':

            if flag == True or float(superheroe_altura["altura"]) < superheroe_altura_minima:

                superheroe_altura_minima = float(superheroe_altura["altura"])

                nombre_superheroe_altura_min = superheroe_altura["nombre"]

                flag = False

    return nombre_superheroe_altura_min

#G)RETORNA EL PROMEDIO ALTURA DE SUPERHEROES MASCULINOS
def obtener_altura_promedio_superheroes_masculino(lista_generica):

    altura_promedio = None
    cont_altura = 0
    acum_altura = 0

    for altura in lista_generica:

        if altura['genero'] == 'M':

            acum_altura = acum_altura + float(altura['altura'])
            cont_altura += 1

    
    altura_promedio = acum_altura / cont_altura

    return altura_promedio

#F)RETORNA EL PROMEDIO ALTURA DE SUPERHEROES FEMENINO
def obtener_altura_promedio_superheroes_femenino(lista_generica):

    altura_promedio = None
    cont_altura = 0
    acum_altura = 0

    for altura in lista_generica:

        if altura['genero'] == 'F':

            acum_altura = acum_altura + float(altura['altura'])
            cont_altura += 1

    
    altura_promedio = acum_altura / cont_altura

    return altura_promedio

#I)RETORNA LOS NOMBRES EN UNA LISTA DE LOS VALORES DE LAS FUNCIONES
def obtener_nombre_altura_maxima_minima(lista_generica):

    lista_nombres = []

    for nombres in lista_generica:

        lista_nombres.append(nombres)
    
    return lista_nombres

    #funciona de esta manera, fuera de la funcion, una lista con funciones a dentro y dentro de cada funcion le asignamos la lista
    """ lista = [obtener_superheroe_mas_alto_femenino(lista_personajes),obtener_superheroe_mas_alto_masculino(lista_personajes),
                obtener_superheroe_mas_bajo_femenino(lista_personajes),obtener_superheroe_mas_bajo_masculino(lista_personajes)] """

#J) OBTIENE LA CANTIDAD DE VECES QUE TIENEN EL MISMO COLOR DE OJOS Y EL TIPO DE COLOR
def obtener_cantidad_color_ojos_superheroe(lista_generica):

    lista_colores_ojos = []
    lista_con_diccionarios = []
    contador = 0

    for elemento in lista_generica:

        elemento['color_ojos'] = elemento['color_ojos'].lower()

        lista_colores_ojos.append(elemento['color_ojos'])

    
    set_color_ojos = set(lista_colores_ojos)

    for color_ojos in set_color_ojos:

        contador = 0

        for heroes in lista_generica:

            heroes['color_ojos'] = heroes['color_ojos'].lower()

            if color_ojos == heroes['color_ojos']:

                contador +=1
        
        diccionario = {}

        diccionario['color_ojos'] = color_ojos

        diccionario['cantidad de superheroes'] = contador

        lista_con_diccionarios.append(diccionario)

    return lista_con_diccionarios

#K) OBTIENE LA CANTIDAD DE VECES QUE TIENEN EL MISMO COLOR DE PELO UN SUPERHEROE
def obtiene_cantidad_color_pelo_superheroe(lista_generica):

    set_tipo_pelos = set()

    for elemento in lista_generica:

        set_tipo_pelos.add(elemento['color_pelo'].lower())

    
    lista_con_diccionario = []
    contador = 0

    for color in set_tipo_pelos:

        diccionario = {}

        diccionario[color] = contador

        for personaje in lista_generica:
            
            if color == personaje['color_pelo'].lower():

                diccionario[color] += 1
        
        lista_con_diccionario.append(diccionario)
                
    return lista_con_diccionario

#L) OBTIENE LA CANTIDAD DE SUPERHEROES QUE TIENE CADA INTELIGENCIA
def obtiene_cantidad_inteligencias_superheroes(lista_generica):

    lista_inteligencias = []
    
    contador_inteligencia = 0

    for elemento in lista_generica:

        lista_inteligencias.append(elemento['inteligencia'])

    lista_inteligencias = set(lista_inteligencias)

    lista_cantidad_heroes = []
    
    for elemento in lista_inteligencias:

        for heroe in lista_generica:

            if elemento == heroe['inteligencia']:

                contador_inteligencia += 1
        
        lista_cantidad_heroes.append(contador_inteligencia)

    lista_de_diccionarios = []

    for inteligencia,cantidad in zip(lista_inteligencias,lista_cantidad_heroes):

        diccionario_new = {}

        diccionario_new['inteligencia'] = inteligencia

        diccionario_new['cantidad heroes'] = cantidad

        lista_de_diccionarios.append(diccionario_new)


    return lista_de_diccionarios
       
#M. Lista todos los superhéroes agrupados por tipo de color de ojos
def obtener_superheroe_color_ojos(lista_generica):

    lista_con_diccionarios = []

    flag_primer_diccionario = False

    for heroes in lista_generica:

        heroes['color_ojos'] = heroes['color_ojos'].lower()

        if flag_primer_diccionario == False:

            diccionario = {}

            lista_nueva = []

            lista_nueva.append(heroes['nombre'])

            diccionario['color_ojos'] = heroes['color_ojos']

            diccionario['nombres'] = lista_nueva

            lista_con_diccionarios.append(diccionario)

            flag_primer_diccionario = True

        else:
            
            flag = False

            for elemento in lista_con_diccionarios:

                if elemento['color_ojos'] == heroes['color_ojos']:

                    elemento['nombres'].append(heroes['nombre'])

                    flag = True

            
            #si no existe ese color de ojos, creamos un diccionario nuevo y lo guardamos en la lista
            if flag == False:

                diccionario = {}

                lista_nueva = []

                lista_nueva.append(heroes['nombre'])

                diccionario['color_ojos'] = heroes['color_ojos']

                diccionario['nombres'] = lista_nueva

                lista_con_diccionarios.append(diccionario)

    
    return lista_con_diccionarios

#N. Lista todos los superhéroes agrupados por tipo de color de pelo 
def obtener_superheroe_color_pelo(lista_generica):


    lista_con_diccionarios = []

    #recorro la lista de superheroes
    for heroes in lista_generica:

        heroes['nombre'] = heroes['nombre'].lower()

        #creo un diccionario por primera vez (TIPO UN FLAG DE MAXIMOS Y MINIMOS)
        if len(lista_con_diccionarios) == 0:

            diccionario_new = {}

            lista_nueva = []

            lista_nueva.append(heroes['nombre'])

            diccionario_new['color_pelo'] = heroes['color_pelo']

            diccionario_new['nombres'] = lista_nueva


            lista_con_diccionarios.append(diccionario_new)
        
        else:

            #asigno un flag harcodeada indicando que no existe ese color de pelo en nuestra lista
            flag = False

            #recorro la lista que cree para poder preguntar si el color de pelo que se encuentra en la lista de personajes
            #tambien se encuentra er nuestra lista
            for diccionario in lista_con_diccionarios:

                if diccionario['color_pelo'] == heroes['color_pelo']:

                    diccionario['nombres'].append(heroes['nombre'])

                    flag = True

            #en caso que no se encuentre, creamos un nuevo diccionario y lo guardamos en nuestra lista
            if flag == False:

                diccionario_new = {}

                lista_nueva = []

                lista_nueva.append(heroes['nombre'])

                diccionario_new['color_pelo'] = heroes['color_pelo']

                diccionario_new['nombres'] = lista_nueva


                lista_con_diccionarios.append(diccionario_new)
            

    return lista_con_diccionarios
            
#O. Lista todos los superhéroes agrupados por tipo de inteligencia            
def obtener_superheroe_inteligencia(lista_generica):

    lista_con_diccionarios = []

    flag_primera_vez = True

    for heroes in lista_generica:

        if flag_primera_vez == True:

            diccionario = {}

            lista_nueva = []

            lista_nueva.append(heroes['nombre'])

            diccionario['inteligencia'] = heroes['inteligencia']

            diccionario['nombres'] = lista_nueva

            lista_con_diccionarios.append(diccionario)

            flag_primera_vez = False
        
        else:

            flag = False

            for elemento in lista_con_diccionarios:

                if elemento['inteligencia'] == heroes['inteligencia']:

                    elemento['nombres'].append(heroes['nombre'])

                    flag = True


            if flag == False:

                diccionario = {}

                lista_nueva = []

                lista_nueva.append(heroes['nombre'])

                diccionario['inteligencia'] = heroes['inteligencia']

                diccionario['nombres'] = lista_nueva

                lista_con_diccionarios.append(diccionario)

    return lista_con_diccionarios













































