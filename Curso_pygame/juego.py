import pygame




pygame.init()

ANCHO_VENTANA = 720

ALTURA_VENTANA = 480

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA))

pygame.display.set_caption('BLOO')

#INICIO EL WHILE
flag_iniciar = True

#POSICION FANTASMA
posicion_personaje = [0,310]
medida_ghost = 100

velocidad = 10
en_suelo = True

#IMG FANTASMA
ghost_right_0 = pygame.image.load('Curso_pygame/walk_right0.png')
ghost_right_0 = pygame.transform.scale(ghost_right_0,(medida_ghost,medida_ghost))
ghost_right_1 = pygame.image.load('Curso_pygame/walk_right1.png')
ghost_right_1 = pygame.transform.scale(ghost_right_1,(medida_ghost,medida_ghost))
ghost_right_2 = pygame.image.load('Curso_pygame/walk_right2.png')
ghost_right_2 = pygame.transform.scale(ghost_right_2,(medida_ghost,medida_ghost))
ghost_right_3 = pygame.image.load('Curso_pygame/walk_right3.png')
ghost_right_3 = pygame.transform.scale(ghost_right_3,(medida_ghost,medida_ghost))

lista_movimiento_right = [ghost_right_0,ghost_right_1,ghost_right_2,ghost_right_3]
indice_img = 0


ghost_left_0 = pygame.image.load('Curso_pygame/walk_left0.png')
ghost_left_0 = pygame.transform.scale(ghost_left_0,(medida_ghost,medida_ghost))
ghost_left_1 = pygame.image.load('Curso_pygame/walk_left1.png')
ghost_left_1 = pygame.transform.scale(ghost_left_1,(medida_ghost,medida_ghost))
ghost_left_2 = pygame.image.load('Curso_pygame/walk_left2.png')
ghost_left_2 = pygame.transform.scale(ghost_left_2,(medida_ghost,medida_ghost))
ghost_left_3 = pygame.image.load('Curso_pygame/walk_left3.png')
ghost_left_3 = pygame.transform.scale(ghost_left_3,(medida_ghost,medida_ghost))

lista_movimiento_left = [ghost_left_0,ghost_left_1,ghost_left_2,ghost_left_3]
indice_img_2 = 0

tipo_movimiento = None

#IMG BOLA DE FUEGO

bola_fuego = pygame.image.load('Curso_pygame/bola_fuego.png')
bola_fuego = pygame.transform.scale(bola_fuego,(100,100))

lanzada = False

posicion_bola = posicion_personaje[:]
velocidad_bola = 10

tiempo_bola_fuego = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo_bola_fuego,200)


#IMG MURCIELAGO

murcielago = pygame.image.load('Curso_pygame/murcielago.png')
murcielago = pygame.transform.scale(murcielago,(50,50))

posicion_murcielago = [720,320]

tiempo_murcielago = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo_murcielago,200)



#registro el tiempo real que paso desde que se inicio el juego
tiempo_imagen = pygame.time.get_ticks()
intervalo_tiempo = 100 

#IMG ESCENARIO


fondo = pygame.image.load('Curso_pygame/fondo_dark.jpeg')
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTURA_VENTANA))

x = 0

tiempo = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo,5)


while flag_iniciar:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            flag_iniciar = False

        #PANTALLA MOVIMIENTO
        if evento.type == tiempo:

            x_relativa = x % ANCHO_VENTANA

            pantalla.blit(fondo,(x_relativa - ANCHO_VENTANA,0))

            if x_relativa < ANCHO_VENTANA:

                pantalla.blit(fondo,(x_relativa,0))

            x -= 1

        if evento.type == tiempo_murcielago:

            if posicion_murcielago[0] >= -10:

                posicion_murcielago[0] -= 2
            
            else:

                posicion_murcielago[0] = ANCHO_VENTANA + 10

        if lanzada == True:

            if evento.type == tiempo_bola_fuego:

                posicion_bola[0] += 3
            
                if posicion_bola[0] >= ANCHO_VENTANA:

                    lanzada = False

        




    #PREGUNTA LOS BOTONES PRESIONADOS
    lista_botones_presionado = pygame.key.get_pressed()

    if lista_botones_presionado[pygame.K_RIGHT]:

        if posicion_personaje[0] < ANCHO_VENTANA:

            posicion_personaje[0] += 2

            tipo_movimiento = 'right'
  

    elif lista_botones_presionado[pygame.K_LEFT]:

        if posicion_personaje[0] > 5:

            posicion_personaje[0] += -2

            tipo_movimiento = 'left'

    elif lista_botones_presionado[pygame.K_SPACE] and en_suelo == True:

        en_suelo = False
        velocidad = -10

    elif lista_botones_presionado[pygame.K_p] and lanzada == False:

        lanzada = True
        velocidad_bola = -10
        posicion_bola[0] = posicion_personaje[0] 
        posicion_bola[1] = posicion_personaje[1]

    else: 

        tipo_movimiento = None


    if not en_suelo:

        posicion_personaje[1] += velocidad

        velocidad += 0.2

        # Verificar si el personaje ha alcanzado el suelo
        if posicion_personaje[1] >= 310:
                
            posicion_personaje[1] = 310
            velocidad = 0
            en_suelo = True


    #consulto el tiempo real
    tiempo_actual = pygame.time.get_ticks()

    #CALCULO EL INTERVALO DE TIEMPO TRANSCURRIDO SI ES IGUAL O MENOR PARA QUE EL PERSONAJE SE MUEVA MAS RAPIDO
    if tiempo_actual - tiempo_imagen >= intervalo_tiempo:
        
        tiempo_imagen = tiempo_actual
        
        if tipo_movimiento == 'right':

            indice_img += 1
                
            if indice_img >= len(lista_movimiento_right):
            
                indice_img = 0

        elif tipo_movimiento == 'left':

            indice_img_2 += 1
                
            if indice_img_2 >= len(lista_movimiento_left):
            
                indice_img_2 = 0

    

    if tipo_movimiento == None:

        pantalla.blit(lista_movimiento_right[0],posicion_personaje)
    
    elif tipo_movimiento == 'right':

        pantalla.blit(lista_movimiento_right[indice_img],posicion_personaje)
    
    else:

        pantalla.blit(lista_movimiento_left[indice_img_2],posicion_personaje)

    #MUESTRO AL MURCIELAGO
    pantalla.blit(murcielago,posicion_murcielago)

    #MUESTRO LA BOLA DE FUEGO
    if lanzada == True:

        pantalla.blit(bola_fuego,posicion_bola)

    pygame.display.flip()
        

pygame.quit()

