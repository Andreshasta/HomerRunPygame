import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Homero(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/1.png'),
				  util.cargar_imagen('imagenes/2.png'),
				  util.cargar_imagen('imagenes/3.png'),
				  util.cargar_imagen('imagenes/4.png'),
                                  util.cargar_imagen('imagenes/5.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(0, 228)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
				self.image = self.imagenes[0]
			elif teclas[K_RIGHT] and self.rect.x<=644-self.rect.width:
				self.rect.x += 10
				self.image = self.imagenes[0]
			if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[1]
				if self.rect.y==0 and self.estado == "subiendo":
					self.puntos = self.puntos + 1
					self.estado = "bajando"
			elif teclas[K_DOWN] and self.rect.y<=362-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[2]
				if self.rect.y==410 and self.estado == "bajando":
					self.puntos = self.puntos + 1
					self.estado = "subiendo"
		else:
			self.image = self.imagenes[4]

