import pygame

pygame.init()

#MEDIDAS DE LA VENTANA
ANCHO_VENTANA = 640
ALTO_VENTANA = 480

#VENTANA
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

#NOMBRE DE LA VENTANA
pygame.display.set_caption('Juego de agustin')

#POSICION CIRCULO MANEJABLE
circulo_posicion = [320,320]

flag_correr = True

while flag_correr:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:

            flag_correr = False

    
    #DEVUELVE TRUE O FALSE SI SE ACUMULAN BOTON CLICKEADOS A LA LISTA
    lista_boton = pygame.key.get_pressed()


    if True in lista_boton:

        if lista_boton[pygame.K_RIGHT]:

            if circulo_posicion[0] < ANCHO_VENTANA + 10:

                circulo_posicion[0] = circulo_posicion[0] + 2

        elif lista_boton[pygame.K_LEFT]:

            if circulo_posicion[0] > ANCHO_VENTANA - 650:

                circulo_posicion[0] = circulo_posicion[0] - 2
            


    
    pantalla.fill((200,0,150))

    pygame.draw.circle(pantalla,(0,220,220),circulo_posicion,50)

    pygame.display.flip()

pygame.quit()

        




    
