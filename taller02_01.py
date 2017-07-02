import sys, pygame
from pygame.locals import *
from Ship import Ship
from Ufo import Ufo


size = width, height = 800, 600
screen = pygame.display.set_mode(size)
def main():
        pygame.init()
        background_image = pygame.image.load("imagenes/space.png")
        background_rect = background_image.get_rect()
        pygame.display.set_caption( "Invaders" )
        ship = Ship(size)
        ufo = Ufo(size)
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                ship.update()
                ufo.update()
                screen.blit(background_image, background_rect)
                screen.blit(ship.image, ship.rect)
                screen.blit(ufo.image, ufo.rect)
                
                pygame.display.update()
                pygame.time.delay(10)
if __name__ == '__main__':
        main()
