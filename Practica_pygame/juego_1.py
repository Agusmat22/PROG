import pygame

pygame.init()

ANCHO_PANTALLA = 640
ALTURA_PANTALLA = 640


pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTURA_PANTALLA))
pygame.display.set_caption('Galaxian')

#IMG NAVE
img_nave = pygame.image.load('Practica_pygame/nave.png')
img_nave = pygame.transform.scale(img_nave,(100,100))

#IMG FONDO
img_fondo = pygame.image.load('Practica_pygame/space.jpg')
img_fondo = pygame.transform.scale(img_fondo,(ANCHO_PANTALLA,ALTURA_PANTALLA))


#POSICION NAVE
posicion_nave = [270,450]


flag_run = True

while flag_run:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:

            flag_run = False

    
    lista_botones_presionado = pygame.key.get_pressed()

    if lista_botones_presionado[pygame.K_RIGHT]:

        if posicion_nave[0] < ANCHO_PANTALLA - 120:

            posicion_nave[0] += 2

    if lista_botones_presionado[pygame.K_LEFT]:

        if posicion_nave[0] >= 4:

            posicion_nave[0] -= 2

        

    pantalla.blit(img_fondo,(0,0)) #fondo

    pantalla.blit(img_nave,posicion_nave) #nave

    pygame.display.flip()


    
pygame.quit()