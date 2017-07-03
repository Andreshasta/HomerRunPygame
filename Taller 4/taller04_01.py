import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "El Cruce" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pierde_vida = util.cargar_sonido('sonidos/pierde_vida.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    control=0
    villano = [Villano((100,80),randint(1,10)),
               Villano((100,150),randint(1,10)),
               Villano((200,220),randint(1,10)),
               Villano((300,300),randint(1,10)),
               Villano((100,350),randint(1,10))]
    m = villano[1]
    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,0,0))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,0,0))
        
        heroe.update()
        for n in villano:
            n.update()

        for n in villano:
            if heroe.rect.colliderect(n.rect) and n != m:
                m=n
                '''print 'colision nueva' '''
                heroe.image = heroe.imagenes[1]
                pierde_vida.play()
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1
                n.velocidad=randint(1,10)
            elif heroe.rect.colliderect(n.rect) and n == m:
                heroe.image = heroe.imagenes[1]
                '''print 'colision antigua' '''
            elif heroe.rect.colliderect(n.rect) == False and n == m:
                m = None
                '''print 'sin colision' '''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,450))
        screen.blit(texto_puntos,(100,450))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__ == '__main__':
      game()
