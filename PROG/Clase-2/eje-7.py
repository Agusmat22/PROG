#Nombre: Agustin Matias Garcia Navas
""" Ejercicio 7:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares. """

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

#En el for asigno una variable "numeros" para que contenga toda la lista_numeros
for numeros in lista_numeros:

    #valido si el numero es par
    if (numeros % 2) == 0:

        print("Los numeros pares son: ", numeros) 
    
    else:

        print("Los numeros impares son: ", numeros)