#test_pygame.py

""" INVESTIGAR COMO PONER VIDEOS """

#CODIGO DE MATIAS
#https://onlinegdb.com/hiqE12E8H
"""

https://onlinegdb.com/K7M4FuH6h
https://onlinegdb.com/aaPFieO0o
https://onlinegdb.com/5KsAqlRrS
"""

import pygame

pygame.init() #Se inicializa pygame

COLOR_ROJO = (255,0,0)


pantalla = pygame.display.set_mode((640,480))#creo la ventana
    
flag_correr = True #Se crea para el while

posicion_circulo = [0,100]

tiempo = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo,100)

while flag_correr:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            flag_correr = False

        if evento.type == pygame.KEYDOWN:

            if evento.type == pygame.K_LEFT:

                posicion_circulo[0] = posicion_circulo[0] - 10

            elif evento.type == pygame.K_RIGHT:

                posicion_circulo[0] = posicion_circulo[0] + 10
            
            elif evento.type == pygame.K_DOWN:

                posicion_circulo[1] = posicion_circulo[1] + 10

            elif evento.type == pygame.K_UP:

                posicion_circulo[1] = posicion_circulo[1] - 10



    pantalla.fill((255,255,255))

    pygame.draw.circle(pantalla,COLOR_ROJO,posicion_circulo,50)

    pygame.display.flip()

pygame.quit()


			
        