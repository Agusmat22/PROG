#nombre: Agustin Matias Garcia Navas
""" Ejercicio 6:
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor. """

lista_numero = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

#creo una variable asignando el valor de la posicion 0 para luego compararlo
numero_mayor = lista_numero[0]

for numero in lista_numero:

#ahora realizo la comparacion y el for va reccorer toda la lista para buscar un numero mayor
    if (numero > numero_mayor):

        numero_mayor = numero
        

print("El numero mayor de la lista es: ", numero_mayor)
