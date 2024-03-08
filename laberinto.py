#CONTROL PRINCIPAL DE NUESTRO CODIGO

#1. Importar el módulo Pygame.
import pygame
import sys
from PersonajePrincipal import PersonajePrincipal
#iniciar PyGame
pygame.init()

#Definimos COLORES
BLANCO = (255,255,255)
VERDE = (0,255,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
NEGRO = (0,0,0)

#definir tamaño de la pantalla
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600

#2. Crear una ventana de aplicación y darle un nombre.
screen = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
pygame.display.set_caption("Juego del Laberinto")


def control_juego(player):

    for event in pygame.event.get():
        #3. Hacer que, cuando se haga clic en la X en la aplicación, la ventana del programa se cierre.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #6. Crear un objeto del personaje principal. Llamar sus métodos de movimiento y renderización y asegurarse de
        #que el programa funcione correctamente y el personaje se mueva con las flechas del teclado
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT:
                player.mover(-2,0)
            elif event.key == pygame.K_RIGHT:
                player.mover(2,0)
            elif event.key == pygame.K_UP:
                player.mover(0,-2)
            elif  event.key == pygame.K_DOWN:
                 player.mover(0,2)
#crear Personajes
player = PersonajePrincipal(50,50,30,30,AZUL)


#JUEGO
while True:
    screen.fill(VERDE)

    control_juego(player)

    player.render(screen)
    pygame.display.flip()

