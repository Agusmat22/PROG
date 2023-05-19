""" EJ 1 debemos lograr tomar un dato por 'input()'
y luego mostrarlo por 'print()'. """
# Para ingresar un dato se utiliza un input
dato = input("Ingrese un dato: ")
""" Para mostrar por pantalla se utiliza print como el console.log """
print(dato)
""" EJ 2 Al ingresar una edad debemos informar si la persona es mayor de edad, sino informar que es un menor de edad. """
edad = input("Ingrese una edad: ")
#con esto parseo la edad a un entero
edad = int(edad)
#siempre se utiliza el " : " al final de la condicion, no se usan llaves ni parensetis como en js
if edad > 17:
    print("Es mayor de edad")
else:
    
    print("Es menor de edad")