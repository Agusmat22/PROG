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

ANCHO_VENTANA = 640
ALTO_VENTANA = 480



pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))#creo la ventana
    
flag_correr = True #Se crea para el while

posicion_circulo = [0,100]

posicion_circulo_auto = [500,0]

posicion_circulo_auto_dos = [250,0]

tiempo = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo,100)

while flag_correr:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            flag_correr = False

        if evento.type == tiempo:

            if posicion_circulo_auto[1] < ALTO_VENTANA + 40 and posicion_circulo_auto_dos[1] < ALTO_VENTANA + 40:

                posicion_circulo_auto[1] = posicion_circulo_auto[1] + 5

                posicion_circulo_auto_dos[1] = posicion_circulo_auto_dos[1] + 5
            
            else:

                posicion_circulo_auto[1] = 0
                posicion_circulo_auto_dos[1] = 0



    lista_boton = pygame.key.get_pressed()

    if True in lista_boton:

        if lista_boton[pygame.K_UP]:

            if posicion_circulo[1] > -2:

                posicion_circulo[1] = posicion_circulo[1] - 2
            
            else:

                posicion_circulo[1] = 480

        elif lista_boton[pygame.K_DOWN]:

            if posicion_circulo[1] < 480 + 40:

                posicion_circulo[1] = posicion_circulo[1] + 2

            else:

                posicion_circulo[1] = 0

        elif lista_boton[pygame.K_LEFT]:

            if posicion_circulo[0] > -20:

                posicion_circulo[0] = posicion_circulo[0] - 2

            else:
                posicion_circulo[0] = 640

        elif lista_boton[pygame.K_RIGHT]:

            if posicion_circulo[0] < 640 + 40:


                posicion_circulo[0] = posicion_circulo[0] + 2

            else:

                posicion_circulo[0] = 0



    pantalla.fill((255,255,255))

    pygame.draw.circle(pantalla,COLOR_ROJO,posicion_circulo,50)

    pygame.draw.circle(pantalla,(0,0,255),posicion_circulo_auto,50)

    pygame.draw.circle(pantalla,(0,0,255),posicion_circulo_auto_dos,50)


    pygame.display.flip()

pygame.quit()


			
        