#test_pygame.py

import pygame

pygame.init() #Se inicializa pygame

running = True #Se crea para el while

window = pygame.display.set_mode((500, 400), 0, 32) #Se crea la ventana

pygame.display.set_caption("vamos a hacer un juego!")

while(running): #WHILE INFINITO
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

    