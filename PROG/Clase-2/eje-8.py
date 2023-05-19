""" Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido """

#NO SE HACERLO
#TENGO QUE REHACERLO CREANDO OTRA LISTA PARA COMPARAR SI HAY IGUALDAD Y AGREGARLO A OTRA VARIABLE REPETIDOS

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

lista_repetido = []


for numeros in lista_numeros:

    #count recorre toda al lista contando los numeros
    #Count devuelve la cantidad de veces que se repite el for (numeros) por eso preguntamos si es mayor a 1 y (and) si este numero no esta (not in) en la lista de repetidos
    if lista_numeros.count(numeros) > 1 and numeros not in lista_repetido:

        #agregamos el numero a la lista de repetidos
        lista_repetido.append(numeros)




print(lista_repetido)

        


