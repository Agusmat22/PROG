#CLONAR UNA LISTA
#CONTROLAR QUE LA MEZCLA SE HAYA RESUELTO

""" Se tiene la siguiente lista ['Manuel', 'Ana', 'Esteban', 'Lia']
mezclar la lista, mostrarla solamente si fue efectivamente mezclada. """

from random import shuffle

lista = ['Manuel', 'Ana', 'Esteban', 'Lia']

def desordenar_lista(lista:list):

    if type(lista) == list and len(lista) > 1:


        lista_copia = lista.copy()

        shuffle(lista_copia)

        if lista_copia != lista:
            
            print(lista_copia)

    
