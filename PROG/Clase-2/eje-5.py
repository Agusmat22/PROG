#NOMBRE: Agustin Matias Garcia Navas
""" Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos """


valor_base_estadia = 15000

descuento = 0

aumento = 0

estacion = input("Ingrese la estacion del año que viajara 'invierno, otoño, primavera o verano': ")

estacion = estacion.lower()

while (estacion != "otoño" and estacion != "invierno" 
        and estacion != "primavera" and  estacion != "verano"):
    
    estacion = input("[ERROR]Ingrese la estacion del año que viajara 'invierno, otoño, primavera o verano': ")

    estacion = estacion.lower()

localidad = input("Ingrese la estacion del año que viajara 'bariloche, cataratas, mar del plata o cordoba': ")

localidad = localidad.lower()

while (localidad != "bariloche" and localidad != "cataratas" 
        and localidad != "mar del plata" and  localidad != "cordoba"):
    
    localidad = input("[ERROR]Ingrese la estacion del año que viajara 'bariloche, cataratas, mar del plata o cordoba': ")

    localidad = localidad.lower()


if (localidad == "bariloche"):

    if (estacion == "invierno"):

        aumento = 1.20
    
    elif (estacion == "verano"):

        descuento = 0.80
    
    else:
        #otoño y primavera

        aumento = 1.10

elif (localidad == "cataratas"):

    if (estacion == "invierno"):

        descuento = 0.90

    else:
        #verano, otoño y primavera
        aumento = 1.10

elif (localidad == "cordoba"):

    if(estacion == "invierno"):

        descuento = 0.90
    
    elif (estacion == "verano"):

        aumento = 1.10

    else: 
        #otoño y primavera no tienen descuento ni aumento
        descuento = 1

else:
    #Mar del plata

    if(estacion == "invierno"):

        descuento = 0.80
    
    elif (estacion == "verano"):

        aumento = 1.20

    else:
        #otoño y primavera

        aumento = 1.10




precio_final = valor_base_estadia * ( descuento + aumento)

precio_final = str(precio_final)

print("El precio final es: " + precio_final)





