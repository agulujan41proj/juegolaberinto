#5. Crear una clase del personaje principal heredada de la clase padre. Para esta clase, implementar un método
#que ocasione el movimiento del personaje con las flechas del teclado.
import pygame
from ObjectoJuego import ObjectoJuego as Objecto
class PersonajePrincipal(Objecto):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        self.velocidad = 15

    def mover(self,aumentarX,aumentarY):
        self.rect.x+= aumentarX*self.velocidad
        self.rect.y+= aumentarY*self.velocidad  