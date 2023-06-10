import pygame
import colores

def crear_titulo_pantalla(ventana,texto,tamaño,x,y,color,valor=None):

    font = pygame.font.SysFont("Secular One", tamaño)

    if valor != None:

        text = font.render(f'{texto}{valor}', True, color)
    else:
        text = font.render(texto, True, color)

    ventana.blit(text,(x,y))
    
