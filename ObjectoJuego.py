import pygame
class ObjectoJuego():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color#4. Crear una clase padre para todos los objetos en el juego.


    #pintar nuestro objecto 
    def render(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
        