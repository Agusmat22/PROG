import pygame
import random
#nave principal
import nave
#nave enemiga
import nave_enemiga
#laser
import laser
#texto
import texto
#niveles
import niveles
#sonido
import sonido
#asteroides
import asteroides

import pantalla_inicio



""" HICE EL INICIO DEL JUEGO, TRATAR DE DISMINUIR CODIGO Y QUE QUEDE MAS LIMPIO """

pygame.init()

ANCHO_VENTANA = 700
ALTURA_VENTANA = 700

#creo ventana del juego
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA))
pygame.display.set_caption('War of Space')


#fondo del juego
lista_fondos = niveles.crear_fondo_niveles(ANCHO_VENTANA,ALTURA_VENTANA,'Galaxian_2\\imagenes\\fondo_inicio.jpg','Galaxian_2\\imagenes\\space_1.jpg','Galaxian_2\\imagenes\\space_2.jpg','Galaxian_2\\imagenes\\space_3.jpg','Galaxian_2\\imagenes\\fondo_final_derrota.jpg')

pantalla_inicio.pantalla_inicio(ventana,lista_fondos) #INICIO DEL JUEGO



#SONIDO DE FONDO
sonido_fondo = sonido.reproducir_sonido('Galaxian_2\\sonido\\Music.wav',0.1)  
sonido_fondo.play(-1) #le paso -1 para que la musica sea de forma indefinida 

#nave principal
nave_principal = nave.Nave('Galaxian_2\\imagenes\\nave.png',90,90,315,600)
score_total = 0

#nave enemiga
lista_naves_enemigas = nave_enemiga.crear_lista_naves(45,45)
#para preguntar por el ID en el for la nave enemiga
numero_id_random = 0



#CREA LISTA DE ASTEROIDES
lista_asteroides = asteroides.crear_lista_asteroides('Galaxian_2\\imagenes\\asteroide.png',40,40)

#boss
boss = nave_enemiga.Boss('Galaxian_2\\imagenes\\boss_1.png',150,150,320,-100)

#FPS
fps = 80
RELOJ = pygame.time.Clock()

#TIEMPO DEL JUEGO GENERAL, AFECTA AL BUCLE
tiempo = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo,20) 


#TIEMPO PARA QUE LOS ENEMIGOS DEMOREN AL DISPARAR
tiempo_transcurrido = 800
tiempo_inicial = pygame.time.get_ticks()

nivel = 0

flag_run = True

while flag_run:

    #indico que den 80 vueltas por segundo en el bucle
    RELOJ.tick(fps)

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:

            flag_run = False
        
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_p:
                #presiona P dispara la nave principal
                nave_principal.disparar()
                         
        #tiempo que pasa en el bucle
        tiempo_actual = pygame.time.get_ticks()

        if nivel == 1: #NIVEL 1, PELEA CONTRA NAVES

            for enemigo in lista_naves_enemigas:

                enemigo.mover(ANCHO_VENTANA)

                enemigo.colision(nave_principal)

                if enemigo.id == numero_id_random:

                    if tiempo_actual - tiempo_inicial > tiempo_transcurrido:

                        enemigo.disparar()
                        #genero un numero random con la cantidad de enemigos para que se vayan turnando al disparar
                        numero_id_random = random.randrange(0,10,1)
                        #lo sumo para que el tiempo actual pueda seguir contando segundos
                        tiempo_inicial = tiempo_actual
        
        elif nivel == 2: #NIVEL 2, ESQUIVAR Y DERRIBAR MEORITOS

            for asteroide in lista_asteroides:

                asteroide.colision(nave_principal)

                pygame.draw.rect(ventana,(255,0,0),asteroide.rect)

                asteroide.mover(ALTURA_VENTANA)
            

        elif nivel == 3:

            boss.mover(ANCHO_VENTANA) #EL BOSS SE MUEVE
            boss.colision(nave_principal) #VALIDO SI EL DISPARO DE LA NAVE PRINCIPAL COLISIONA CON EL BOSS


            if tiempo_actual - tiempo_inicial > tiempo_transcurrido:

                boss.disparar()

                #lo sumo para que el tiempo actual pueda seguir contando segundos
                tiempo_inicial = tiempo_actual

                boss.velocidad_disparo += 0.09 #aumento la velocidad del disparo

        
        print(boss.velocidad_disparo)

        botones_presionados = pygame.key.get_pressed()

        if botones_presionados[pygame.K_RIGHT]:

            nave_principal.mover('right',ANCHO_VENTANA)
        
        elif botones_presionados[pygame.K_LEFT]:

            nave_principal.mover('left',ANCHO_VENTANA)



    nivel = niveles.actualizar_nivel(ventana,lista_fondos,lista_naves_enemigas,nave_principal,ALTURA_VENTANA,boss,lista_asteroides) #ACTUALIZA LA PANTALLA GENERAL CON LOS NIVELES

    texto.crear_titulo_pantalla(ventana,'Score: ',40,20,20,(255,255,255),nave_principal.score)
    #pygame.draw.rect(ventana,(255,0,0),nave_principal.rect)

    score_total = nave_principal.score  #guardo el score
    print(nave_principal.vida)
    #actualiza los cambio
    pygame.display.flip()


pygame.quit()