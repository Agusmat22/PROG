#NOMBRE: Agustin Matias GArcia Navas
""" Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5] """
""" 
flag = 0
lista_nombre = ["Juan","Pedro","Sol","Paco","Ana"]
lista_sexo = ["m","m","f","m","f"]
lista_nota = [6,8,10,8,5] """

""" while (flag < 5):

    nombre = input("Ingrese su nombre: ")

    while (nombre == ""):

        nombre = input("[ERROR]Ingrese su nombre: ")

    lista_nombre.append(nombre)

    sexo = input("Ingrese su sexo: ")

    while (sexo != "f" and sexo != "m"):

        sexo = input("[ERROR]Ingrese su sexo: ")

    lista_sexo.append(sexo)
    
    nota = input("Ingrese la nota")

    while (nota == ""):

        sexo = input("[ERROR]Ingrese la nota: ")

    nota = int(nota)

    lista_nota.append(nota)
    



    flag += 1 """

""" Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5] """

flag = True
lista_nombre = ["Juan","Pedro","Sol","Paco","Ana"]
lista_sexo = ["m","m","f","m","f"]
lista_nota = [6,3,10,8,6]

#hombres
cont_h = 0

#mujeres
acum_notas_mujeres = 0
cont_m = 0

flag_m = True
cont_minimo_m = 0

for listas_notas in lista_nota:

    #hombres
    if lista_sexo[cont_h] == "m":


        if flag == True or listas_notas < nota_mas_baja_h:

            nota_mas_baja_h = listas_notas
            posicion = cont_h
            flag = False
        

    else:
    #mujeres

        acum_notas_mujeres += listas_notas
        cont_m += 1

        if flag_m == True or listas_notas < nota_min_mujeres:

            nota_min_mujeres = listas_notas 
            posicion_mujeres = cont_minimo_m
            flag_m = False
        
    #CONTADORES SIEMPRE AL FINAL DEL CODIGO Y FUERA DEL IF SI HAY DOS CASO EJ HOMBRES Y MUJERES
    cont_h += 1
    cont_minimo_m += 1




    

print(f'El hombre con la nota mas baja es {lista_nombre[posicion]} y su nota fue de {lista_nota[posicion]}')

print(f'La mujer con la nota mas baja es {lista_nombre[posicion_mujeres]} y su nota fue de {lista_nota[posicion_mujeres]}')

promedio_notas_mujeres = acum_notas_mujeres / cont_m

print(f'El promedio de notas de mujeres es de {promedio_notas_mujeres}')




    

            







    