import pygame
import texto
import clases_genericas
import colores

def pantalla_inicio(ventana,lista_fondos):

    flag_inicio = True

    foto_titulo = clases_genericas.Imagen('Galaxian_2\\imagenes\\titulo_inicio.png',550,70,70,150)

    while flag_inicio: #pantalla de inicio

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                flag_inicio = False
                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:

                    flag_inicio = False

        lista_fondos[0].update(ventana)
        foto_titulo.update(ventana)
        texto.crear_titulo_pantalla(ventana,'Presione "espacio" si desea jugar',40,130,340,colores.BLANCO_BEIGE)
        pygame.display.flip()