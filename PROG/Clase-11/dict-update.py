#METODO UPDATE()
#Actualiza el contenido de una Key de un diccionario, pero si no existe, la agrega.

#EJEMPLO SI NO EXISTE:
lista = [
    {"edad":25,"nota":9},
    {"nombre":"Jose","edad":34,"nota":8},
    {"nombre":"Sol","edad":46,"nota":7},
    {"nombre":"Beto","edad":28,"nota":6}
    ]

for e_nombre in lista:
    print(e_nombre.get("nombre", "SIN NOMBRE"))    

dicCero = lista[0]
dicCero.update({"nombre": "Soy Matias"})
lista[0]= dicCero
print(lista)

#EJEMPLO SI EXISTE:
lista = [
    {"edad":25,"nota":9},
    {"nombre":"Jose","edad":34,"nota":8},  #->Va a reemplazar el nombre
    {"nombre":"Sol","edad":46,"nota":7},
    {"nombre":"Beto","edad":28,"nota":6}
    ]

for e_nombre in lista:
    print(e_nombre.get("nombre", "SIN NOMBRE"))    


dicCero = lista[1]
dicCero.update({"nombre": "Soy Matias"})
lista[1]= dicCero
print(lista)

