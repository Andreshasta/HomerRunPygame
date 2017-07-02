import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Bullet(Sprite):
    def __init__(self, pos):
        Sprite.__init__(self)
        self.vel = [0,-2]
        self.image = pygame.image.load("imagenes/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
    def update(self):
        self.rect = self.rect.move(self.vel)
