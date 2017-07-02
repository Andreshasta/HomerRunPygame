import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Ufo(Sprite):
    def __init__(self, cont_size):
        Sprite.__init__(self)
        self.puntos = 0
        self.vida = 100
        self.cont_size = cont_size
        self.image = pygame.image.load("imagenes/ufo.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]/2, 0)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT] and self.rect.left > 0:
            self.rect.x -= 10
        elif teclas[K_RIGHT] and self.rect.right < self.cont_size[0]:
            self.rect.x += 10
        elif teclas[K_UP]:
            pass
        elif teclas[K_DOWN]:
            pass
