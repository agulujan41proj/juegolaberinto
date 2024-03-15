import pygame
from objectoJuego import ObjectoJuego
class Meta(ObjectoJuego):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        