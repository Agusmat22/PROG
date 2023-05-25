#Busca y elimina la key, que se pasa como parámetro, 
#de un diccionario y devuelve su valor, si no existe, da error.
#Para que eso no suceda, se puede utilizar el segundo parámetro 
#de pop() que es el valor por defecto si la key no existe.
lista = [
    {"edad":25,"nota":9},
    {"nombre":"Jose","edad":34,"nota":8},
    {"nombre":"Sol","edad":46,"nota":7},
    {"nombre":"Beto","edad":28,"nota":6}
    ]

for e_nombre in lista:
    print(e_nombre.get("nombre", "SIN NOMBRE"))    

dic_cero = lista[0]
valor_eliminado = dic_cero.pop("nombre","NO EXISTE")
print("Valor eliminado = ", valor_eliminado)

