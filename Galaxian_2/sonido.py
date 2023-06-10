import pygame

def reproducir_sonido_fondo(sonido,volumen):

    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(sonido)
    sonido_fondo.set_volume(volumen)
    
    return sonido_fondo

def reproducir_sonido(sonido,volumen):

    pygame.mixer.init()
    sonido = pygame.mixer.Sound(sonido)
    sonido.set_volume(volumen)
    
    return sonido

