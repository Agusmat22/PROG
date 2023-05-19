""" Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven """

edad = [25,36,18,23,45,14]
nombre = ["Juan","Ana","Sol","Mario","Sonia","julieta"]
#cont para saber la posicion del elemento
flag = False
cont = 0

#la variable edades va recorrer la lista edad

for edades in edad:

    if flag == False or edades < edad_mas_joven:

        edad_mas_joven = edades
        posicion = cont
        flag = True
    
    cont += 1

print(f'El nombre de la persona mas joven es {nombre[posicion]} y su edad es {edad[posicion]} años')



       











