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
              
        a= [10]
        for i in range(1,11):
                if i<11:
                        print i
                        ufo.rect.left=ufo.rect.left+40
                        a.insert(i,ufo.rect.left)
                        print a
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                    
                ship.update()
                ufo.update()
                                                        
                screen.blit(background_image, background_rect)
                screen.blit(ship.image, ship.rect)
                for x in a:
                        ufo.rect.left=x
                        screen.blit(ufo.image, ufo.rect)
                        ufo.update()
                pygame.display.update()
                pygame.time.delay(10)
                
if __name__ == '__main__':
        main()
