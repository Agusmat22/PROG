#NOMBRE: Agustin Matias Garcia Navas
""" Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años). """

edad = input("Ingrese una edad: ")

edad = int(edad)

while (edad < 0):

    edad = input("[ERROR]Ingrese una edad: ")
    edad = int(edad)


if (edad > 17):

    print("Usted es mayor de edad")

elif (edad > 12):

    print("Usted es adolecente")

else:

    print("Usted es un niño")

