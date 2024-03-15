#CONTROL PRINCIPAL DE NUESTRO CODIGO

#1. Importar el módulo Pygame.
import pygame
import sys
from personajePrincipal import PersonajePrincipal
from pared import Pared
from meta import Meta
from enemigo import Enemigo
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

#cargaDeImagenes
victoriaImagen = pygame.image.load('imagenes/victoria.jpg')
perdisteImagen = pygame.image.load('imagenes/perdiste.jpg')
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
def crearParedes():
    listaParedes = []
    pared1 = Pared(200,20,10,400,ROJO)
    listaParedes.append(pared1)
    pared2 = Pared(300,PANTALLA_ALTO-20-400,10,400,ROJO) 
    listaParedes.append(pared2)
    pared3 = Pared(400,20,10,400,ROJO)
    listaParedes.append(pared3)
    pared4 = Pared(500,PANTALLA_ALTO-20-400,10,400,ROJO) 
    listaParedes.append(pared4)
    return listaParedes
def renderizarParedes(screen,listaParedes):
    for pared in listaParedes:
        pared.render(screen)
def chocaPared(listaParedes,player):
    for pared in listaParedes:
        if player.rect.colliderect(pared.rect):
            return True
    return False
def crearEnemigos():
    listaEnemigos = []
    enemigo1 = Enemigo(50,480,30,30,NEGRO,"x",50,100)
    listaEnemigos.append(enemigo1)
    enemigo2 = Enemigo(250,20,30,30,NEGRO,"y",50,100)
    listaEnemigos.append(enemigo2)
    enemigo3 = Enemigo(350,480,30,30,NEGRO,"y",50,100)
    listaEnemigos.append(enemigo3)
    enemigo4 = Enemigo(450,20,30,30,NEGRO,"x",50,100)
    listaEnemigos.append(enemigo4)
    return listaEnemigos
def renderizarEnemigos(listaEnemigos,screen):
    for enemigo in listaEnemigos:
        enemigo.render(screen)
def moverEnemigos(listaEnemigos):
    pass
#crear Personajes
player = PersonajePrincipal(50,50,30,30,AZUL)
meta = Meta(700,300,30,30,BLANCO)
listaParedes = crearParedes()
listaEnemigos = crearEnemigos()
#JUEGO
running = True
while running:
    screen.fill(VERDE)

    control_juego(player)
    moverEnemigos(listaEnemigos)

    #chocando nuestros personajes
    if player.rect.colliderect(meta.rect):
        screen.blit(victoriaImagen,(0,0))
        running = False
    elif chocaPared(listaParedes,player):
        screen.blit(perdisteImagen,(0,0))
        running = False
    else:
        player.render(screen)
        meta.render(screen)
        renderizarParedes(screen,listaParedes)
        renderizarEnemigos(listaEnemigos,screen)
    pygame.time.delay(30)
    pygame.display.flip()


