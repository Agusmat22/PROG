
""" Al ingresar una edad debemos informar si la persona es mayor de edad (mas de 18 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años). """



#TENER CUIDADO CON HACER ESPACIO Y TABULAR, SIEMPRE HAY QUE SACAR EL ESPACIO EN BLANCO

edad = input("Ingrese una edad: ")

edad = int(edad)

#operadores logicos  && = and , || = or y not

#elif es como un else if

if edad > 17:

    print("Es mayor de edad")

else:

    if edad > 12:

        print("Es adolecente")

    else:

        print("Es un niño")











