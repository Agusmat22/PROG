#NOMBRE: Agustin Matias Garcia Navas
""" Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.' """

edad = input("Ingrese una edad: ")

edad = int(edad)

while (edad < 0):

    edad = input("[ERROR]Ingrese una edad: ")

    edad = int(edad)

estado_civil = input("Ingrese su estado civil: ")

estado_civil = estado_civil.lower()

while (estado_civil == ""):

    estado_civil = input("[ERROR]Ingrese su estado civil: ")
    estado_civil = estado_civil.lower()

if (edad < 18 and estado_civil != "soltero"):

    print("Es muy pequeño para NO ser soltero")

else:

    print("Muy bien que esta soltero")


