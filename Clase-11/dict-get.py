#METODO GET()
#SI TENGO UN DICCIONARIO SIN UNA CLAVE NOS DA 
#ERROR EL PROGRAMA AL IMPRIMIR LOS VALORES DE LAS KEYS

lista = [
    {"edad":25,"nota":9},
    {"nombre":"Jose","edad":34,"nota":8},
    {"nombre":"Sol","edad":46,"nota":7},
    {"nombre":"Beto","edad":28,"nota":6}
    ]
"""
DA ERROR
"""
#for e_nombre in lista:
#    print(e_nombre["nombre"])

#CON EL METODO GET(), MUESTRA EL VALOR POR DEFECTO O NONE

for e_nombre in lista:
    print(e_nombre.get("nombre", "SIN NOMBRE"))    

for i,e_nombre in enumerate(lista):
    nom = e_nombre.get("nombre","no hay nombre")

    if nom == ("no hay nombre"):
        vacio = i
        print("posicion sin key: ", i)
        

