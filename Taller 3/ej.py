import sys, pygame
from pygame.locals import *
from Ship import Ship
from Ufo2 import Ufo


size = width, height = 800, 600
screen = pygame.display.set_mode(size)
def main():
        pygame.init()
        background_image = pygame.image.load("imagenes/space.png")
        background_rect = background_image.get_rect()
        pygame.display.set_caption( "Invaders" )

        
        ship = Ship(size)
        ufos = []
        for i in range(0,2):
            ufos.append([])
            for j in range(0,10):
                ufos[i].append(Ufo(size, j, 10, i*20))
     
        """for i in range(0,10):
                 ufos.append(Ufo(size, i, 10))"""
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                ship.update()
                screen.blit(background_image, background_rect)
                screen.blit(ship.image, ship.rect)
                for bullet in ship.bullets:
                        bullet.update()
                        for linea in ufos:
                                for ufo in linea:
                                        if bullet.rect.colliderect(ufo.rect):
                                                ship.bullets.remove(bullet)
                                                '''ufos.remove(ufo)'''
                                                linea.remove(ufo)
                        if bullet.rect.top <= 0:
                                ship.bullets.remove(bullet)
                        screen.blit(bullet.image, bullet.rect)
                for linea in ufos:
                        for ufo in linea:
                                ufo.update()
                                screen.blit(ufo.image, ufo.rect)
                pygame.display.update()
                pygame.time.delay(10)
                
if __name__ == '__main__':
        main()
