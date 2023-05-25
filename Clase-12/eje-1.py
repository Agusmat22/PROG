#CODIGO DE MARINA PRIMERA CLASE DE PROGRAMACION ORIENTADA OBJETOS
# https://onlinegdb.com/nDviaGufV

#CODIGO DE RENATO
# https://onlinegdb.com/yKePmpUXD

class Persona:

    tipo = 'Humano'

    def __init__(self,nombre,edad,peso) -> None:

        self.nombre = nombre
        self.__edad = edad
        self.__peso = peso
        #USAR '__' SIGNIFICA QUE ESTA MODO PRIVADO SOLO SE PUEDE ACCEDER CON METODOS DENTRO DE LA CLASES Y HEREDADO


    def __str__(self) -> str:
        
        return f'Mi nombre es: {self.nombre} '
    
    #PROPERTY ME SIRVE PARA MOSTRAR POR UN PRINT EJ UN METODO SIN UTILIZAR LOS PARENTESIS AL FINAL
    
    
    #CON ESTE METODO AL MOMENTO DE CREARSE LA INSTANCIA PUEDO ACCEDER A LOS ATRIBUTOS EN PRIVADO


    #GETTER PUEDO MOSTRAR EL ATRIBUTO EN PRIVADO Y SIN CORCHETES
    @property
    def edad(self): #GETTER

        return self.__edad
    
    #PERMITO MODIFICAR EL ATRIBUTO QUE SE ENCUENTRA EN PRIVADO
    @edad.setter
    def edad(self,item):
        
        self.__edad = item

    def __gt__(self,item):

        return self.edad > item.edad
    

    


persona_1 = Persona('juan',100,70)

persona_2 = Persona('juan',40,70)

valor = persona_1 > persona_2

print(persona_1)


        