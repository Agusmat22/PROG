import pygame


#explosion de la nave
def explosion_nave(alto,ancho):
    explo_1 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 1.png')
    explo_1 = pygame.transform.scale(explo_1,(ancho,alto))
    explo_2 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 2.png')
    explo_2 = pygame.transform.scale(explo_2,(ancho,alto))
    explo_3 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 3.png')
    explo_3 = pygame.transform.scale(explo_3,(ancho,alto))
    explo_4 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 4.png')
    explo_4 = pygame.transform.scale(explo_4,(ancho,alto))
    explo_5 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 5.png')
    explo_5 = pygame.transform.scale(explo_5,(ancho,alto))
    explo_6 = pygame.image.load('Juegos\\juego_1.py\\explosion\\explo 6.png')
    explo_6 = pygame.transform.scale(explo_6,(ancho,alto))

    lista = [explo_1,explo_2,explo_3,explo_4,explo_5,explo_6]

    return lista


indice_animacion = 0
tiempo_animacion = 100  # Duración de cada fragmento en milisegundos
tiempo_acumulado = 0

clock = pygame.time.Clock()

class Explosion:

    def __init__(self, lista_animaciones, x, y, tiempo_animacion):
        self.lista_animaciones = lista_animaciones
        self.x = x
        self.y = y
        self.tiempo_animacion = tiempo_animacion
        self.indice_animacion = 0
        self.tiempo_acumulado = 0
        self.imagen = self.lista_animaciones[self.indice_animacion]

    def update(self, tiempo_transcurrido):
        self.tiempo_acumulado += tiempo_transcurrido
        if self.tiempo_acumulado >= self.tiempo_animacion:
            self.tiempo_acumulado = 0
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.lista_animaciones):
                return True
            self.imagen = self.lista_animaciones[self.indice_animacion]
        return False

    def actualzar_pantalla(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))
