import pygame

pygame.init()


ANCHO_VENTANA = 680
ALTURA_VENTANA = 480

#CREO LA VENTANA
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA))
pygame.display.set_caption('Juego free')

flag_run = True

#posicion circulo
posicion_circle = [50,50]

#CREO UN TIMER
tiempo_segundos = pygame.USEREVENT
pygame.time.set_timer(tiempo_segundos,100)

#CREAR UN TEXTO
fuente = pygame.font.SysFont('Arial',30)
texto = fuente.render('Hola soy agus',True,(0,255,0))


while flag_run:

    lista_evento = pygame.event.get()

    for evento in lista_evento:

        if evento.type == pygame.QUIT:

            flag_run = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            #PASO LA POSICION DEL CLICK DEL MOUSE EN PANTALLA
            #CASTEO EL EVENTO PORQUE DEVUELVE UNA TUPLA Y LO PASO A LISTA
            posicion_circle = list(evento.pos)

        #PREGUNTO SI ES DEL TIPO TIMER
        if evento.type == pygame.USEREVENT:

            #AHORA PREGUNTO SI ES IGUAL A EL TIEMPO QUE YO CREE
            if evento.type == tiempo_segundos:

                if posicion_circle[0] < ANCHO_VENTANA + 30:

                    posicion_circle[0] += 10
                
                else:
                    posicion_circle[0] = -30
        
        #PREGUNTO SI SE PRESIONO UNA TECLA
        #ESTA FORMA HAY QUE CLICKEAR REITERADAS VECES EL TECLADO, NO SE PUEDE MANTENER PRESIONADO
        #LA TECLA
        if evento.type == pygame.KEYDOWN:

            #PREGUNTO SI FUE LA TECLA DOWN
            if evento.key == pygame.K_DOWN:

                if posicion_circle[1] < ALTURA_VENTANA:

                    posicion_circle[1] += 15

                else:

                    posicion_circle[1] = 50


    # OTRA ALTERNATIVA PARA PRESIONAR TECLAS A DIFERENCIAS QUE ESTA RECONOCE
    # CUANDO MANTENEMOS PRESIONADA UNA TECLA

    lista_botones_presionados = pygame.key.get_pressed()

    if lista_botones_presionados[pygame.K_UP]:

        if posicion_circle[1] > 0:

            posicion_circle[1] -= 5

        else:

            posicion_circle[1] = ALTURA_VENTANA + 30 

        
    #DOY COLOR AL FONDO
    ventana.fill((255,0,0))

    #CREO EL CIRCULO
    pygame.draw.circle(ventana,(0,0,0),posicion_circle,30)

    ventana.blit(texto,(10,30))

    pygame.display.flip()

pygame.quit()

