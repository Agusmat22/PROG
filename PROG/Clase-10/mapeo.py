#UN MAPEO numero reales Y QUE HAGA UN DESCUENTO DEL 15% A LOS NUMEROS


""" Se tiene la siguiente lista = [100.00, 200.00, 400.00, 800.00] mapearla realizando un descuento del 15%
a cada elemento de lista. Por ultimo mostrar la lista mapeada. """

def calcular_porcentaje_lista(lista:list,porcentaje:float):

    if type(lista) == list and type(porcentaje) == int or type(porcentaje) == float:


        #LAMBDA ES UNA FUNCION SENCILLA(LA CREE PARA SACAR EL PORCENTAJE DE CADA VALOR DENTRO DE LA LISTA)
        #MAP PASA COMO PARAMETRO A OTRA FUNCION EN CADA UNO DE LOS ELEMENTOS
        lista_resultado = list(map(lambda a : -a*porcentaje/100 + a ,lista))

        return(lista_resultado)


lista = [100.00, 200.00, 400.00, 800.00]

a = calcular_porcentaje_lista(lista,10)
print(a)