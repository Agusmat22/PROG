#importo los datos del archivo data.py a este archivo
from data import lista_bzrp

""" EJERCICIOS

1)MOSTRAR LOS NOMBRES DE LAS SESSIONS
2)MOSTRAR EL VIDEO CON MENOS VIEWS
3)MOSTRAR EL VIDEO CON MAS VIEWS
4)CREAR UN MENU

"""




""" Esta funcion muestra los titulos de las canciones """
def mostrar_titulo_canciones():
    for titulos in lista_bzrp:

        print("Titulo:",titulos["title"])


""" Esta funcion muestra la cancion con menos visitas de la lista """
def mostrar_visitas_min():
    flag = True
    video_min_views = None
    nombre_video_min_views = None

    for visitas in lista_bzrp:

        if flag == True or float(visitas["views"]) < video_min_views:

            video_min_views = float(visitas["views"])
            nombre_video_min_views = visitas["title"]
            flag = False
    
    print("Titulo:",nombre_video_min_views,", Visitas:",video_min_views)

def mostrar_visitas_max():
    flag = True
    video_max_views = None
    nombre_video_max_views = None

    for visitas in lista_bzrp:

        if flag == True or float(visitas["views"]) > video_max_views:

            video_max_views = float(visitas["views"])
            nombre_video_max_views = visitas["title"]
            flag = False
    
    print("Titulo:",nombre_video_max_views,", Visitas:",video_max_views)

        
#CREE UNA FUNCION GENERICA PARA QUE PUEDA SER REUTILIZABLE CON CUALQUIER MENU,
#EL PARAMETRO ES PARA INGRESAR EL MENU QUE QUERRAMOS, TOMA UN DATO X INPUT Y RETORNA EL VALOR
def menu_opciones(lista):

    for menus in lista:

        print(menus)

    opcion = input("Elija una opcion: ")

    return opcion


continuar = True

#creo mi menu para esta app
lista_menu = ['1)MOSTRAR LOS NOMBRES DE LAS SESSIONS','2)MOSTRAR EL VIDEO CON MENOS VIEWS','3)MOSTRAR EL VIDEO CON MAS VIEWS', '4)SALIR']


while continuar == True:

    opcion_elegida = menu_opciones(lista_menu)

    opcion_elegida = int(opcion_elegida)


    if opcion_elegida == 1:

        mostrar_titulo_canciones()
    
    elif opcion_elegida == 2:

        mostrar_visitas_min()

    elif opcion_elegida == 3:

        mostrar_visitas_max()

    elif opcion_elegida == 4:
        print("Usted selecciono salir, Muchas gracias por utilizar nuestra sistema")
        break







