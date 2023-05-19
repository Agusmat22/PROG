#NOMBRE: Agustin Matias Garcia Navas
""" 3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
 edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero)
 cantidad de carreras ganadas (no pueden ser números negativos)
 número del vehículo (no puede ser un número negativo)
se necesita saber:
*Nacionalidad del piloto más joven.
*Cantidad de vehículos con número par.
*Nombre del piloto con menos victorias y el número de auto impar.
*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
*Nombre del piloto más joven con más victorias.
*Nacionalidad del piloto más veterano con menos victorias.
*Promedio de edad de los pilotos que tiene un vehículo con número par. """

flag = 0

#A)
flag_a = 0

#B)
cant_vehiculos_par = 0

#C)
flag_c = 0

#D)
cant_pilotos_mayores_d = 0

#E)
flag_e = 0

#G)
acum_edad_total = 0
cont_pilotos_ingresados = 0


while flag < 2:

    flag += 1

    nombre = input("Ingrese su nombre: ")

    while nombre == "":

        nombre = input("[ERROR]Ingrese su nombre: ")


    edad = input("Ingrese su edad: ")

    edad = int(edad)

    while edad < 0:

        edad = input("[ERROR]Ingrese su edad: ")

        edad = int(edad)


    nacionalidad_piloto = input("Ingrese la nacionalidad del piloto: ")

    nacionalidad_piloto = nacionalidad_piloto.lower()

    while nacionalidad_piloto != "argentino" and nacionalidad_piloto != "ingles" and nacionalidad_piloto != "frances" and nacionalidad_piloto != "brasilero":

        nacionalidad_piloto = input("[ERROR]Ingrese la nacionalidad del piloto: ")

        nacionalidad_piloto = nacionalidad_piloto.lower()


    cant_carreras_ganadas = input("Ingrese la cantidad de carreras ganadas: ")

    cant_carreras_ganadas = int(cant_carreras_ganadas)

    while cant_carreras_ganadas < 0:

        cant_carreras_ganadas = input("[ERROR]Ingrese la cantidad de carreras ganadas: ")

        cant_carreras_ganadas = int(cant_carreras_ganadas)

    numero_vehiculo = input("Ingrese el numero vehiculo: ")

    numero_vehiculo = int(numero_vehiculo)

    while numero_vehiculo < 0:

        numero_vehiculo = input("[ERROR]Ingrese el numero vehiculo: ")

        numero_vehiculo = int(numero_vehiculo)

    
    #A) *Nacionalidad del piloto más joven.

    if flag_a == 0:

        flag_a =1

        edad_mas_joven = edad

        nacionalidad_mas_joven = nacionalidad_piloto
    
    elif edad < edad_mas_joven:

        edad_mas_joven = edad

        nacionalidad_mas_joven = nacionalidad_piloto

    
    #B)*Cantidad de vehículos con número par.

    if (numero_vehiculo % 2)== 0:

        cant_vehiculos_par += 1 

        #G) *Promedio de edad de los pilotos que tiene un vehículo con número par. """

        acum_edad_total = edad

        cont_pilotos_ingresados += 1


    
    #C) *Nombre del piloto con menos victorias y el número de auto impar.

    if flag_c == 0 and (numero_vehiculo % 2) != 0:

        nombre_piloto_menos_victorias = nombre

        cant_min_carreras_ganadas = cant_carreras_ganadas

        flag_c = 1

    elif (numero_vehiculo % 2) != 0:


        if cant_carreras_ganadas < cant_min_carreras_ganadas:

            nombre_piloto_menos_victorias = nombre

            cant_min_carreras_ganadas = cant_carreras_ganadas

    #D) *Cantidad de pilotos mayores de 25 años con número de vehículo impar.

    if edad > 25 and (numero_vehiculo % 2) == 0:

        cant_pilotos_mayores_d += 1

    #E) *Nombre del piloto más joven con más victorias.
    #F) *Nacionalidad del piloto más veterano con menos victorias.
    if flag_e == 0:

        nombre_mas_joven = nombre

        cant_max_victorias = cant_carreras_ganadas

        nacionalidad_mas_veterano = nacionalidad_piloto

        cant_min_victorias = cant_carreras_ganadas

        flag_e = 1

    elif cant_carreras_ganadas > cant_max_victorias:

        nombre_mas_joven = nombre
        
        cant_max_victorias = cant_carreras_ganadas
    
    elif cant_carreras_ganadas < cant_min_victorias:

        nacionalidad_mas_veterano = nacionalidad_piloto

        cant_min_victorias = cant_carreras_ganadas


    





#A)
print("La nacionalidad del piloto mas joven es:",nacionalidad_mas_joven)


#B)
print("La cantidad de vehiculos con numero par es:",cant_vehiculos_par)

#C)
print("El nombre del piloto con menos victorios es:", nombre_piloto_menos_victorias)

#D)
print("La cantidad de pilotos mayores de 25 años son:", cant_pilotos_mayores_d)

#E)
print("El nombre del piloto mas joven es:", nombre_mas_joven)

#F)
print("La nacionalidad del piloto mas veterano es:", nacionalidad_mas_veterano)

#G) *Promedio de edad de los pilotos que tiene un vehículo con número par. """

promedio_edad = acum_edad_total / cont_pilotos_ingresados

print("El promedio de edad de pilotos con numeros par es de :",promedio_edad)
