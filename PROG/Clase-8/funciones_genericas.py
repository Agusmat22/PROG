import re
import json


""" CREAR Y GUARDAR ARCHIVOS """

#ABRE UN ARCHIVO JSON Y RETORNA UNA LISTA
def abrir_json(nombre:str):

    with open(nombre,'r') as archivo:

        diccionario = {}

        diccionario = json.load(archivo)

        return diccionario['heroes']

#ABRE ARCHIVO CSV Y RETORNA UNA LISTA (MODIFICAR LOS PATRONES SEGUN REQUERIMOS)
def abrir_csv(nombre:str):

    with open(nombre,'r') as archivo:

        lista_elementos = []

        for elemento in archivo:
            
            diccionario = {}

            linea = re.split(',',elemento)


            diccionario['nombre'] = linea[0]
            diccionario['edad'] = linea[1]
            diccionario['apellido'] = linea[2]
            diccionario['altura'] = re.sub('\n','',linea[3])

            lista_elementos.append(diccionario)

        return lista_elementos



#CREAR UN ARCHIVO JSON
def crear_archivo_json(nombre:str,lista:list,clave:str):

    with open(nombre,'w') as archivo:

        clave = {lista}

        json.dump(clave,archivo)


#CREAR UN ARCHIVO CSV Y GUARDA EL CONTENIDO
def crear_archivo_csv(nombre:str,lista:list):

    with open(nombre, 'w+') as archivo:

        valor = validar_lista(lista)

        if valor == True:

            for personaje in lista:

                contenido = str(personaje['id']) +','+ personaje['nombre'] +','+ personaje['plataforma'] +','+ personaje['modo'] +','+ personaje['empresa'] +','+ str(personaje['anio']) +','+ personaje['pais'] +','+ personaje['genero'] + '\n'

                archivo.write(contenido)

            valor_retorno = 'Se guardo correctamente'
        else:

            valor_retorno = 'Error en la lista'

        print(valor_retorno)



""" SANITIZAR Y NORMALIZAR """


#SANITIZAR UN NUMERO FLOTANTE O ENTERO
def sanitizar_numero(numero:str):

    if type(numero) == str:

        if numero != "":

            if re.search('^[0-9]+$',numero):

                numero = int(numero)

                valor_retorno = numero
            
            elif re.search('^[0-9]+\.[0-9]+$',numero):

                numero = float(numero)

                valor_retorno = numero
            
            else:

                valor_retorno = 'La cadena contiene caracteres no numericos'

        else:
            valor_retorno = 'La cadena se encuentra vacia'

    
    else:

        valor_retorno = 'El dato ingresado no es de tipo str'


    if type(valor_retorno) == str:

        print(valor_retorno)

    else:

        return valor_retorno


#SANITIZAR UN STRING
def sanitizar_string(dato:str)->str:

    if type(dato) == str:

        if re.search('^(\s*[a-z],?+\s*-?[a-z]*\.?)+$',dato,re.IGNORECASE):
            dato = dato.strip()

            dato = re.sub('-',' ',dato)

            dato = re.sub(',',' ',dato)

            lista_dato = re.split(' ',dato)

            cadena = ""

            for palabra in lista_dato:

                if palabra != "":

                    cadena += palabra.lower() + ' '


            valor_retorno = cadena[:-1]

        elif re.search('',dato,re.IGNORECASE):

            valor_retorno = 'N/A'

        else:

            valor_retorno = 'El dato contiene caracteres no alfabeticos'
    
    else:

        valor_retorno = 'Error en el tipo de dato'

    return valor_retorno


#SANITIZA LA KEY DE UNA LISTA SEGUN LE PASEMOS POR PARAMETRO, REUTILIZA FUNCION DE (sanitizar numero)
def normalizar_numero_lista(lista:list,key:str)->list:

    valor_retorno = None

    if type(lista) == list and len(lista) > 0:

        for i in lista:

            if key in i:

                i[key] = sanitizar_numero(i[key])

            else:

                valor_retorno = 'La key no se encuentra en el diccionario'
                break

    else:

        valor_retorno = 'Error en la lista ingresada'


    if valor_retorno != None:

        print(valor_retorno)
    
    else:

        valor_retorno = lista

        return valor_retorno


#NORMALIZA LAS CADENAS DE TEXTO DENTRO UN UNA LISTA CON DICCIONARIO
def normalizar_texto_lista(lista:list,clave:str)->list:

    if type(lista) == list:
        
        valor_retorno = None

        for elemento in lista:

            if clave in elemento:

                elemento[clave] = sanitizar_string(elemento[clave])

            else:

                valor_retorno = 'La clave no existe en el diccionario'
                break

    else: 
        valor_retorno = 'La lista ingresada no es del tipo list'
        

    if valor_retorno != None:

        print(valor_retorno)

    else:

        return lista



"""VALIDACIONES """


#VALIDA UNA LISTA
def validar_lista(lista:list)->bool:

    if type(lista) == list:

        if len(lista) > 0:

            valor_retorno = True

        else:
            
            valor_retorno = False
            
    else:

        valor_retorno = False

    
    return valor_retorno


#VALIDA SI EL DATO CONTIENE SOLAMENTE NUMEROS
def validar_numero(numero:str)->bool:

    if type(numero) == str:

        if numero != "":

            if re.search('^[0-9]+$',numero):

                valor_retorno = True
            else:
                valor_retorno = False

        else:
            valor_retorno = False
    
    else:
        valor_retorno = False

    return valor_retorno


""" IMPRIMIR DATOS """

#MUESTRA UN MENU DE OPCIONES
def imprimir_menu_opciones(mensaje:str):

    print(mensaje)


#IMPRIME UNA LISTA CON EL NOMBRE DEL HEROE Y SI QUEREMOS OTRA CLAVE CON SU VALOR
def imprimir_lista(lista:list,clave = None):

    mensaje = ""

    for i in lista:

        if 'nombre' in i:

            if clave != None:

                mensaje += 'Nombre: '+i['nombre'] +' | '+ clave+': '+ str(i[clave])+'\n'

            else:
                mensaje += 'Nombre: '+i['nombre'] +'\n'
        
    print(mensaje)   


""" PEDIR DATOS """


#PIDE UN DATO POR INPUT Y LO RETORNA
def pedir_dato(mensaje:str):

    if type(mensaje) == str and mensaje != '':

        valor = input(mensaje)

    else:

        valor = 'No ingreso un string'

    return valor


""" CALCULAR PROMEDIO, MAXIMOS Y MINIMOS E ORDENAMIENTOS """    


#CALCULA EL PROMEDIO DE CUALQUIER KEY DENTRO DE UNA LISTA
def calcular_promedio(lista:list,clave:str):

    if type(lista) == list and len(lista) > 0:

        contador_elementos = 0

        cantidad_keys = 0

        for heroe in lista:

            if clave in heroe:

                cantidad_keys += heroe[clave]
                contador_elementos +=1

        promedio = cantidad_keys / contador_elementos

        valor_retorno = promedio
    
    else:

        valor_retorno = 'Error'

    return valor_retorno


#CALCULA EL MAXIMO A MINIMO DE UNA LISTA CON KEY, PREGUNTA SI QUEREMOS MAXIMO O MINIMO
def calcular_maximo_minimo(lista:list,key:str)->int:

    opcion = pedir_dato('Desea calcular el minimo o maximo? ')

    while re.search('^(?!maximo$|minimo$)',opcion):

        opcion = pedir_dato('ERROR Desea calcular el minimo o maximo? ')


    dato = None
    flag = True

    for i in lista:

        if key in i:

            if flag == True:

                dato = i[key]
                flag = False
            
            else:

                if opcion == 'maximo' and i[key] > dato:

                    dato = i[key]

                elif opcion == 'minimo' and i[key] < dato:

                    dato = i[key]

        else:
            dato = 'La clave no existe en el diccionario'
            break


    
    if type(dato) == str:

        print(dato)
    
    else:

        return dato


#CALCULA LA CANTIDAD DE VECES QUE SE REPITE UNA KEY 'STR' DENTRO UNA LISTA Y RETORNA UNA LISTA CON DICCIONARIOS
def obtener_keys_repetidas(lista:list,clave:str)->list:

    valor_retorno = None
    lista_keys = []

    for i in lista:

        if clave in i:

            lista_keys.append(i[clave].lower())
        
        else:

            valor_retorno = "La clave no existe en el diccionario"
            break
    
    if valor_retorno == None:

        lista_keys = set(lista_keys)

        lista_keys_repetidas = []

        for keys in lista_keys:

            diccionario = {}
            
            contador = 0

            for i in lista:

                if i[clave].lower() == keys:

                    contador += 1
            

            diccionario[keys] = contador

            lista_keys_repetidas.append(diccionario)

        valor_retorno = lista_keys_repetidas



    if type(valor_retorno) == str:

        print(valor_retorno)

    else:

        return valor_retorno


#ORDENA UNA LISTA SEGUN LA KEY INGRESADA
def ordenar_lista_keys(lista:list,clave:str):

    opcion = pedir_dato("Desea ordenar de forma asc o desc? ")

    while re.search('^(?!asc$|desc$)',opcion,re.IGNORECASE):

        opcion = pedir_dato("ERROR Desea ordenar de forma asc o desc? ")

    flag = True

    while flag == True:

        flag = False

        for i in range(len(lista)-1):

            if clave in lista[i] and clave in lista[i+1]:

                if opcion.lower() == "asc" and lista[i][clave] > lista[i+1][clave]:

                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    flag = True
                
                elif opcion.lower() == "desc" and lista[i][clave] < lista[i+1][clave]:

                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    flag = True

    return lista
    

#LISTA QSORT
def ordenar_qsort(lista:list)->list:

    lista_derecha = []
    lista_izquierda = []

    if len(lista) <= 1:

        return lista
    else:

        pivote = lista[0]

        for elemento in lista[1:]:

            if elemento > pivote:

                lista_derecha.append(elemento)

            else:

                lista_izquierda.append(elemento)

            

    lista_izquierda = ordenar_qsort(lista_izquierda)
    lista_izquierda.append(pivote)
    lista_derecha = ordenar_qsort(lista_derecha)

    return lista_izquierda + lista_derecha

            
