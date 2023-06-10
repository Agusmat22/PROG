import pygame
import random

#SEGUIR COMPLETANDO

def crear_lista_asteroides(img,ancho,alto):

    lista_asteroides = []

    for i in range(10):

        velocidad = random.randrange(2,6,1) #le doy una velocidad random de movimiento

        asteroide_nuevo = Asteroide(img,ancho,alto,velocidad)

        lista_asteroides.append(asteroide_nuevo)

    return lista_asteroides


def actualizar_lista_asteroides(lista_asteroides:list,ventana):

    for asteroide in lista_asteroides:

        asteroide.update(ventana)

def eliminar_lista_asteroides(lista_asteroides):

    for asteroide in lista_asteroides:

        lista_asteroides.remove(asteroide) #elimina todos los asteroides


class Asteroide:  #creo el asteroide

    def __init__(self,img,ancho,alto,velocidad) -> None:
        
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(ancho,alto))
        
        self._rect = self._superficie.get_rect()
        self._rect.y = random.randrange(-1000,-100,70)
        self._rect.x = random.randrange(10,670,70)
        self._velocidad = velocidad #velocidad a la que baja el asteroide


    def mover(self,altura_ventana):

        if self._rect.y < altura_ventana + 50:

            self._rect.y += self._velocidad

        else:

            self._rect.y = random.randrange(-1000,-100,70)
            self._rect.x = random.randrange(10,670,70)

    def colision(self,nave_principal):

        if self._rect.colliderect(nave_principal.laser.rect):

            self._rect.y = random.randrange(-1000,-100,70)
            self._rect.x = random.randrange(10,670,70)
            
            nave_principal.disparo = False #cancelo el disparo ya que colisiono
            nave_principal.laser.rect.y = -2000 #MODIFICO LA POSICION DEL LASER AL COLISIONAR PARA QUE DESAPAREZCA DE LA IMAGEN
            nave_principal.score += 1 #POR CADA DISPARO ME SUMO UN PUNTO AL SCORE 
        
        elif nave_principal.rect.colliderect(self._rect): #pregunta si algun asteroide toco a la nave principal

            nave_principal.vida -= 1
            self._rect.y = random.randrange(-1000,-100,70)
            self._rect.x = random.randrange(10,670,70)


    def update(self,ventana):

        ventana.blit(self._superficie,(self._rect))


    @property
    def superficie(self):

        return self._superficie
    
    @property
    def rect(self):

        return self._rect


