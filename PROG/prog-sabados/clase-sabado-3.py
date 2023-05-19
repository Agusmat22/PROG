import re 

#NOMBRE: AGUSTIN MATIAS GARCIA NAVAS

""" 1.Verificar correo electrónico: Crea una función que tome una cadena de texto como
argumento y verifique si se trata de una dirección de correo electrónico válida. Una
dirección de correo electrónico válida debe tener un formato como
'usuario@dominio.com' """

correo = 'usuario@dominio.com'

def verificar_correo(dato:str):


    if re.search('^[a-z]{5,14}@[a-z]{5,14}\.com$',dato):

        valor_retorno = dato
    
    else:

        valor_retorno = 'Mail incorrecto'

    return valor_retorno


""" 2.Eliminar dígitos: Crea una función que tome una cadena de texto y elimine todos los
dígitos que contiene. """

texto = 'agustin tiene hambre'

def eliminar_digitos(dato:str):

    if type(texto) == str:

        cadena_vacia = re.sub('.+','',texto)

        return cadena_vacia
    
""" 3.Validar formato de fecha: Crea una función que tome una cadena de texto como
argumento y verifique si se trata de una fecha válida en formato 'dd/mm/aaaa' . """

fecha = '24/02/2001'

def validar_fecha(dato:str):

    if type(dato) == str:

        if re.search('^[0-9]{2}/[0-9]{2}/[0-9]{4}',dato):

            return dato


""" 4.Reemplazar formato de fecha: Crea una función que tome una cadena de texto que
contiene una fecha en formato 'dd/mm/aaaa' y la reemplace por la misma fecha en
formato 'mm/dd/aaaa'. """

def reemplazar_formato_fecha(dato:str):

    if type(dato) == str:

        if re.search('^[0-9]{2}/[0-9]{2}/[0-9]{4}',dato):


            fecha_dia_mes = re.findall('[0-9]+',dato)
                
            fecha_reemplazada = fecha_dia_mes[1] +'/'+fecha_dia_mes[0] +'/'+ fecha_dia_mes[2]
            

            return fecha_reemplazada
        

""" 5.Validar número de teléfono: Escribe una expresión regular que valide un número de
teléfono con el siguiente formato: '+54 9 11 1234-5678'. La expresión regular debe
aceptar números de teléfono con el código de país '+54', seguido de un espacio, el
dígito 9, otro espacio, el código de área de dos dígitos, un espacio, el número de
teléfono de ocho dígitos separado por un guión en la mitad. """

telefono = '+54 9 11 1234-5678'

def validar_numero(dato:str):

    if type(dato) == str:

        if re.search('^\+[0-9]{2} 9 [0-9]{2} [0-9]{4}-[0-9]{4}$',dato):

            return dato

""" 6.Validar CUIL: Escribe una expresión regular que valide un CUIL con el siguiente
formato: "20-12345678-1". La expresión regular debe aceptar CUILS que comiencen con
"20" seguido de un guión, ocho dígitos y otro guión, seguido del último dígito que es un
verificador. """

cuil = "20-12345678-1"

def validar_cuil(dato:str):

    if type(dato) == str:

        if re.search('^[0-5]{2}-[0-9]{8}-[0-9]$',dato):

            return dato





