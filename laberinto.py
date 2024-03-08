#CONTROL PRINCIPAL DE NUESTRO CODIGO

#1. Importar el módulo Pygame.
import pygame
import sys
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


def control_juego():

    for event in pygame.event.get():
        #3. Hacer que, cuando se haga clic en la X en la aplicación, la ventana del programa se cierre.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#JUEGO
while True:
    screen.fill(VERDE)

    control_juego()

    pygame.display.flip()

