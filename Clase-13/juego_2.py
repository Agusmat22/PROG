import pygame

pygame.init()

#COLORES
COLOR_ROJO = (255,0,0)
COLOR_BLANCO =(255,255,255)

#VENTANA
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

#EVENTO DE TIEMPO
tiempo = pygame.USEREVENT + 0
pygame.time.set_timer(tiempo,100)


#TITULO DEL JUEGO
pygame.display.set_caption('Rambix')

#CIRCULOS AUTOMATICOS
pos_circulo_1 = [1000,50]
pos_circulo_3 = [1000,500]

#triangualo
pos_triangulo = [100,240]

#IMAGENES DE MESSI
medida_messi = 200

img_messi_pelota = pygame.image.load('Clase-13/messi_con_pelota.png')
img_messi_pelota = pygame.transform.scale(img_messi_pelota,(medida_messi,medida_messi))

img_messi_celebrando = pygame.image.load('Clase-13/messi_celebrando.png')
img_messi_celebrando = pygame.transform.scale(img_messi_celebrando,(200,200))

img_messi_llora = pygame.image.load('Clase-13/messi_llora.png')
img_messi_llora = pygame.transform.scale(img_messi_llora,(150,150))

#IMAGENES DE DEFENSORES
img_defensor_1 = pygame.image.load('Clase-13/defensor1.png')
img_defensor_1 = pygame.transform.scale(img_defensor_1,(200,200))

img_defensor_2 = pygame.image.load('Clase-13/defensor2.png')
img_defensor_2 = pygame.transform.scale(img_defensor_2,(200,200))

#IMAGEN ARCO

img_arco = pygame.image.load('Clase-13/arco.png')
img_arco = pygame.transform.scale(img_arco,(400,200))
img_arco = pygame.transform.rotate(img_arco,270)


#ESTADIO
estadio = pygame.image.load('Clase-13/estadio.jpg')
estadio = pygame.transform.scale(estadio,(ANCHO_VENTANA,ALTO_VENTANA))

gol= False

flag_correr = True

flag_rebote = True

tocan_messi = False

disparo = False

posicion_balon = [pos_triangulo[0],pos_triangulo[1]]

while flag_correr:


    #CREO EL RECTANGULO DE LA FOTO
    rectangulo_messi = img_messi_pelota.get_rect()
    rectangulo_messi.centerx = pos_triangulo[0]#medida x
    rectangulo_messi.centery = pos_triangulo[1] #medida y

    rectangulo_defensor1 = img_defensor_1.get_rect()
    rectangulo_defensor1.centerx = pos_circulo_1[0] #medida x
    rectangulo_defensor1.centery = pos_circulo_1[1] #medida y



    lista_evento = pygame.event.get()

    for evento in lista_evento:

        if evento.type == pygame.QUIT:

            flag_correr = False

        if evento.type == tiempo:


            if pos_circulo_3[0] > 20:

                pos_circulo_1[0] = pos_circulo_1[0] - 15
                pos_circulo_3[0] = pos_circulo_3[0] - 15
        
            else:

                pos_circulo_1[0] = ANCHO_VENTANA - 20 
                pos_circulo_3[0] = ANCHO_VENTANA - 20
                

            if disparo == True and posicion_balon[0] < ANCHO_VENTANA - 20:

                posicion_balon[0] = posicion_balon[0] + 30

            else:

                disparo = False


                    


    
    lista_botones_presionado = pygame.key.get_pressed()

    if True in lista_botones_presionado:

        if lista_botones_presionado[pygame.K_RIGHT]:

            if pos_triangulo[0] < ANCHO_VENTANA - 150:

                pos_triangulo[0] = pos_triangulo[0] + 4

            if pos_triangulo[0] > ANCHO_VENTANA-150:

                gol = True
 

        if lista_botones_presionado[pygame.K_LEFT]:

            if pos_triangulo[0] > ANCHO_VENTANA - ANCHO_VENTANA:

                pos_triangulo[0] = pos_triangulo[0] - 4

        if lista_botones_presionado[pygame.K_UP]:

            if pos_triangulo[1] > ALTO_VENTANA - ALTO_VENTANA:

                pos_triangulo[1] = pos_triangulo[1] - 4
            

        if lista_botones_presionado[pygame.K_DOWN]:

            if pos_triangulo[1] < ALTO_VENTANA - 150:

                pos_triangulo[1] = pos_triangulo[1] + 4

        if lista_botones_presionado[pygame.K_p]:


            disparo = True

        
        if rectangulo_messi.colliderect(rectangulo_defensor1):

            tocan_messi = True



    #FONDO DE LA VENTANA
    #pantalla.fill((estadio))

    #FONDO DE PANTALLA CON IMAGEN
    pantalla.blit(estadio, (0, 0))
    
    #ARCO
    pantalla.blit(img_arco, (1080, 160))
    
    #CIRCULOS AUTOMATICOS
    pantalla.blit(img_defensor_1,pos_circulo_1)
    pantalla.blit(img_defensor_2,pos_circulo_3)


    if disparo == True:

        pygame.draw.circle(pantalla,(255,0,0),pos_triangulo,20)

    if gol == False and tocan_messi == False:

        pantalla.blit(img_messi_pelota,pos_triangulo)
    
    elif tocan_messi == True:
        
        pantalla.blit(img_messi_llora,pos_triangulo)

    elif gol == True:
        
        pantalla.blit(img_messi_celebrando,pos_triangulo)
    



    #EJECUTA TODOS LOS CAMBIOS A LA VEZ
    pygame.display.flip()




pygame.quit()