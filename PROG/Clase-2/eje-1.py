#NOMBRE: Agustin Matias Garcia Navas
""" Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona. """

nombre = input("Ingrese el nombre: ")

while (nombre == ""):

    nombre = input("[ERROR]Ingrese el nombre: ")

sueldo = input("Ingrese el sueldo: ")

while (sueldo == ""):

    sueldo = input("[ERROR]Ingrese el sueldo: ")

sueldo = int(sueldo)

#aumento 10%
sueldo_con_aumento = sueldo * 1.10

sueldo_con_aumento = str(sueldo_con_aumento)

print("El aumento de: "+ nombre + " es de: "+ sueldo_con_aumento+ " pesos")