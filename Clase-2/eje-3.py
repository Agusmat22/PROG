#NOMBRE: Agustin Matias Garcia Navas
""" Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos. """

flag = 0

#A)
cont_numeros_pares = 0
cont_numeros_impares = 0

#B)
flag_menor_numero = True

#C)
flag_mayor_numero = True

#D)
acum_numeros_positivos = 0


while flag < 5:

    flag += 1

    numero = input("Ingrese un numero: ")

    numero = int(numero)


    #A)
    if ((numero % 2) == 0):

        cont_numeros_pares += 1

        #C)
        if (flag_mayor_numero == True):

            numero_mayor = numero
            flag_mayor_numero = False
        
        elif (numero > numero_mayor):

            numero_mayor = numero

    else:

        cont_numeros_impares += 1


    #B)
    if (flag_menor_numero == True):

        flag_menor_numero == False

        numero_menor = numero
    
    elif (numero < numero_menor):

        numero_menor = numero


    #D)

    if (numero > 0):

        acum_numeros_positivos += numero


#a. Cantidad de pares e impares.

cont_numeros_pares = str(cont_numeros_pares)
cont_numeros_impares = str(cont_numeros_impares)

print("La cantidad de numero pares son: "+ cont_numeros_pares+ " y los impares son: "+ cont_numeros_impares)

#b. El menor número ingresado.

numero_menor = str(numero_menor)

print("El numero menor ingresado es: "+ numero_menor)

#c. De los pares el mayor número ingresado.

numero_mayor = str(numero_mayor)

print("El numero mayor ingresado dentro de los pares es: "+ numero_mayor)

#d. Suma de los positivos.

acum_numeros_positivos = str(acum_numeros_positivos)

print("La acumulacion de numero positivos ingresados es: "+ acum_numeros_positivos)






