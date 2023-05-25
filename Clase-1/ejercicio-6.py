#NO se utiliza CamelCase, ahora para asignar una viariable vamos a utilizar el _ ej:  nombre_colegio

""" Pedir números hasta que el USUARIO QUIERA e informar la suma acumulada y el promedio. """


flag_numero = "si"
cont_numero = 0
acum_numero = 0


while flag_numero == "si":

    numero = input("Ingrese un numero: ")

    numero = int(numero)

    acum_numero = acum_numero + numero

    cont_numero += 1

    flag_numero = input("Desea continuar? 'si o no' ")

#para tener el cociente se puede usar el //
promedio_numero = acum_numero / cont_numero

#pasamos los NUMBER a STRING para poder concatenar el mensaje en PRINT
acum_numero = str(acum_numero)

promedio_numero = str(promedio_numero)

print("La cantidad total de numeros acumulados es: "+ acum_numero)

print("La cantidad total de numeros acumulados es: "+ promedio_numero)


#la otra forma de mostrar un mensaje y no pasar a string los NUMBER

""" 
print("La cantidad total de numeros acumulados es: ")

print(acum_numero)

print("La cantidad total de numeros acumulados es: ")

print(promedio_numero) 
"""
