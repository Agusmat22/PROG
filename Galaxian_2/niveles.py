import pygame
import nave_enemiga
import asteroides


def crear_fondo_niveles(ancho,alto,fondo_inicio,fondo_1,fondo_2,fondo_3,fondo_final):

    #fondo de pantalla
    fondo_inicio = Nivel(fondo_inicio,ancho,alto)
    fondo_nivel_1 = Nivel(fondo_1,ancho,alto)
    fondo_nivel_2 = Nivel(fondo_2,ancho,alto)
    fondo_nivel_3 = Nivel(fondo_3,ancho,alto)
    fondo_final_juego = Nivel(fondo_final,ancho,alto)

    lista_fondos = [fondo_inicio,fondo_nivel_1,fondo_nivel_2,fondo_nivel_3,fondo_final_juego]

    return lista_fondos

def actualizar_nivel(ventana,lista_fondos,lista_naves_enemigas,nave_principal,altura_ventana,boss,lista_asteroides):

    nivel = None

    if nave_principal.score < 3: #NIVEL 1
        nivel = 1

        lista_fondos[1].update(ventana)

        #actualizo las naves enemigas en el nivel 1
        nave_enemiga.actualizar_pantalla_lista_enemigos(lista_naves_enemigas,ventana,altura_ventana)

    
    elif nave_principal.score < 10: #NIVEL 2

        nave_enemiga.eliminar_naves_enemigas(lista_naves_enemigas)   #cambio de nivel y elimino todas las naves enemigas
        lista_fondos[2].update(ventana)
        asteroides.actualizar_lista_asteroides(lista_asteroides,ventana)
        
        nivel = 2

    elif nave_principal.score < 15:

        asteroides.eliminar_lista_asteroides(lista_asteroides) #elimino los asteroides para que no aparezcan el el siguien nivel

        lista_fondos[3].update(ventana)
        boss.update(ventana,altura_ventana)

        nivel = 3

    nave_principal.update(ventana) #nave principal siempre la actualizo no importa el nivel
    
    return nivel



class Nivel:

    def __init__(self,imagen,ancho,alto) -> None:
        
        self._fondo = pygame.image.load(imagen)
        self._fondo = pygame.transform.scale(self._fondo,(ancho,alto))

    def update(self,ventana):

        ventana.blit(self._fondo,(0,0))
