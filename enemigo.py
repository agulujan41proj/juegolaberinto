import pygame
from objectoJuego import ObjectoJuego
class Enemigo(ObjectoJuego):
    def __init__(self, x, y, width, height, color,desplazamiento,inicioX,recorrido):
        super().__init__(x, y, width, height, color)
        self.desplazamiento = desplazamiento
        self.inicioX = inicioX
        self.recorrido = recorrido
        self.velocidad = 2
        self.adelante = True
    def mover(self,aumentarX,aumentarY):
        self.rect.x+= aumentarX*self.velocidad
        self.rect.y+= aumentarY*self.velocidad 

    def moverEnemigo(self):
        if self.desplazamiento == "x":
            if self.rect.x <= (self.inicioX + self.desplazamiento):
                self.mover(self.velocidad,0)
        #falta completar