#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS

import re

# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
#(terrestre, anfibio, volador)

lista = [{'terrestre': ['leon','perro','gato','elefante']},
         {'anfibio': ['tiburon','delfin','orca']},
         {'volador': ['aguila','cuervo','paloma']}]

""" # 2 Imprimir la lista completa de animales con su tipo. """
def imprimir_lista_tipo(dato:list):

    for tipo in dato:

        for key,value in tipo.items():

            print(f'TIPO: {key.upper()}: {value}')

""" # 3 Mostrar el porcentaje de animales por tipo. """

def calcular_porcentaje_animal(dato:list):

    cont_terrestre = 0
    cont_anfibio = 0
    cont_volador = 0

    for tipo in dato:

        for clave,valor in tipo.items():
            


            if clave == 'terrestre':

                for i in valor:
                    cont_terrestre += 1
            
            elif clave == 'anfibio':

                for i in valor:
                    cont_anfibio += 1
            
            else:

                for i in valor:
                    cont_volador += 1
            
    
    contador_animales_totales = cont_terrestre + cont_anfibio + cont_volador

    porcentaje_terrestre = cont_terrestre * 100 / contador_animales_totales

    porcentaje_anfibio = cont_anfibio * 100 / contador_animales_totales

    porcentaje_volador = cont_volador * 100 / contador_animales_totales

    print(f'El porcentaje del terrestre es: {porcentaje_terrestre}%\n'
          f'El porcentaje del anfibio es: {porcentaje_anfibio}%\n'
          f'El porcentaje del volador es: {porcentaje_volador}%\n'
          )



