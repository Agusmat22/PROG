from copy import deepcopy

lista = [['hola','hello'],5,6,20]

lista_2 = deepcopy(lista)

print(lista)

lista_2[0][1]= 'cambie'
print(lista_2)