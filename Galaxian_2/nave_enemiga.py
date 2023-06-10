import pygame
import random
import laser
from nave import Nave



def crear_lista_naves(ancho,alto):

    lista_naves_enemigas = []

    for i in range(10):

        x = random.randrange(10,670,35)
        y = random.randrange(-500,-100,35)

        nave_enemiga = NaveEnemiga('Galaxian_2\\imagenes\\nave_enemiga.png',ancho,alto,x,y,i)

        lista_naves_enemigas.append(nave_enemiga)

    return lista_naves_enemigas

#actualiza la lista de enemigos
def actualizar_pantalla_lista_enemigos(lista_enemigos,ventana,alto_ventana):

    for nave_enemiga in lista_enemigos:

        nave_enemiga.update(ventana,alto_ventana)

#elimina todas las naves
def eliminar_naves_enemigas(lista_naves):

    for nave in lista_naves:

        lista_naves.remove(nave)


class NaveEnemiga(Nave):

    def __init__(self,img,ancho,alto,x,y,id) -> None:
        super().__init__(img,ancho,alto,x,y)

        self._laser = laser.Laser('Galaxian_2\\imagenes\\laser_red.png',5,20)   #guardo el objeto en un atributo, preguntar al profesor si esta bien!!!!
        self._id = id
        self._direcion_movimiento = 'right'
        self._posicion_final_y = random.randrange(10,400,50)   #indico el tope hasta donde puede bajar la nave
        self._velocidad = 2 #velocidad de moviemiento



    def mover(self,ancho_ventana):
        
        if self._rect.y < self._posicion_final_y:

            self._rect.y += 3

        if self._direcion_movimiento == 'right' and self._rect.x < ancho_ventana - 50:

            self._rect.x += self._velocidad

        else:
            self._direcion_movimiento = 'left'   #'left' = izquierda


            if self._direcion_movimiento == 'left' and self._rect.x > 0:

                self._rect.x -= self._velocidad

            else:

                self._direcion_movimiento = 'right' 

    def disparar(self):
        
        if not self._disparo and self._rect.y > 10:

            self._disparo = True
            self._laser.rect.x = self._rect.x + 20
            self._laser.rect.y = self._rect.y + 34

    def colision(self,nave_principal):

        if self._vida > 0 and self._rect.colliderect(nave_principal.laser.rect):  #pregunto si colisiono el laser de la nave principal con la nave enemiga

            self._rect.x  = random.randrange(10,670,35)
            self._rect.y  = random.randrange(-300,-100,35)
            nave_principal.disparo = False #si colisiona el laser de la nave principal desaparece
            nave_principal.laser.rect.y = 2000
            nave_principal.score += 1
            self._vida -= 1


        elif nave_principal.rect.colliderect(self._laser.rect): #pregunto si la nave_principal colisiono con el laser enemigo

            nave_principal.vida -= 1

            self._laser.rect.y = 2000
            


    def update(self,ventana,alto_ventana):

        #valido que la nave no hay colisionado con un laser
        if self._vida > 0:

            if self._disparo == True:

                if self._laser.rect.y < alto_ventana:
                        
                    #velocidad del disparo
                    self._laser.rect.y += self._velocidad_disparo
                
                else:

                    self._disparo = False

                #ACTUALIZO EL LASER SIEMPRE Y CUANDO ESTE EN EJECUCION
                ventana.blit(self._laser.superficie,self._laser.rect)


            #actualiza la nave
            ventana.blit(self._superficie,(self._rect))


    @property
    def id(self):

        return self._id
    

#EL BOSS
class Boss(NaveEnemiga):

    def __init__(self, img, ancho, alto, x, y) -> None:
        super().__init__(img, ancho, alto, x, y,id) #heredo el valor de mi clase padre

        self._rect.y = -100
        self._posicion_final_y = 200
        self._direcion_movimiento_vertical = 'down'
        self._vidas = 10 #le creo el atributo vidas para que resista a 6 disparos
        self._laser = laser.Laser('Galaxian_2\\imagenes\\bola_poder_2.png',50,40)
        self._velocidad = 3 #velocidad de moviemiento


    def mover(self,ancho_ventana): 

        #modifico el tipo de movimiento respecto a las naves enemigas
        if self._direcion_movimiento_vertical == 'down' and self._rect.y < self._posicion_final_y: #baja

            self._rect.y += 3

        else:

            self._direcion_movimiento_vertical = 'up'

            if self._direcion_movimiento_vertical == 'up' and self._rect.y > 0: #sube

                self._rect.y -= 3
            else:

                self._direcion_movimiento_vertical = 'down'

        if self._direcion_movimiento == 'right' and self._rect.x < ancho_ventana - 150:

            self._rect.x += self._velocidad

        else:
            self._direcion_movimiento = 'left'   #'left' = izquierda


            if self._direcion_movimiento == 'left' and self._rect.x > 0:

                self._rect.x -= self._velocidad

            else:

                self._direcion_movimiento = 'right'


    def disparar(self):

        if not self._disparo and self._rect.y > 10:

            self._disparo = True
            self._laser.rect.x = self._rect.x + 35
            self._laser.rect.y = self._rect.y + 110
    
    
    def colision(self, nave_principal):

        if self._vida > 0 and self._rect.colliderect(nave_principal.laser.rect):

            self._vidas -=1 #le resto una vida
            
            nave_principal.disparo = False #si colisiona el laser de la nave principal desaparece
            nave_principal.laser.rect.y = 2000
            nave_principal.score += 1

            if self._vidas == 0:
                self._nave_visible = False
                self._rect.y  = 3000 #random.randrange(-300,1000,35) (no me acuerdo porque hice esto, NO ELIMINAR POR AHORA)
                self._laser.rect.x = 3000
                self._laser.rect.y = 3000
    
        elif nave_principal.rect.colliderect(self._laser.rect): #pregunto si la nave_principal colisiono con la bola de poder del boss

            nave_principal.vida -= 1
            
            self._laser.rect.y = 2000 #EL DISPARO DEL ENEMIGO LO SACO DE LA VENTANA ASI NO ME SIGUE IMPACTANDO

    def update(self, ventana, alto_ventana):

        #valido que la nave no hay colisionado con un laser
        if self._vida > 0:

            if self._disparo == True:

                if self._laser.rect.y < alto_ventana:
                        
                    #velocidad del disparo
                    self._laser.rect.y += self._velocidad_disparo
                
                else:

                    self._disparo = False

                #ACTUALIZO EL LASER SIEMPRE Y CUANDO ESTE EN EJECUCION
        ventana.blit(self._laser.superficie,self._laser.rect)


            #actualiza la nave
        ventana.blit(self._superficie,(self._rect))


