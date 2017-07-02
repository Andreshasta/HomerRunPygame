import sys, pygame, util
from pygame.locals import *
from Homero import *
from Obstaculo import *
from random import *
SCREEN_WIDTH = 644
SCREEN_HEIGHT = 362
ICON_SIZE = 32


def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "HomerRun" )
    background_image = util.cargar_imagen('imagenes/Springfield.jpg');
    pierde_vida = util.cargar_sonido('sonidos/Douh.wav')
    tema=util.cargar_sonido('sonidos/simpson.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Homero()
    control=0
    villano = [Barril((100,10),randint(1,5)),
               Barril((100,79),randint(1,5)),
               Barril((200,148),randint(1,5)),
               Barril((300,217),randint(1,5)),
               Barril((100,286),randint(1,5))]

    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,0,0))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,0,0))
        
        heroe.update()
        
        for n in villano:
            n.update()
        
        for n in villano:
            
            if heroe.rect.colliderect(n.rect) and control==0:
                control=1
                heroe.image = heroe.imagenes[3]
                pierde_vida.play()
                if heroe.vida > 0:
                    heroe.vida=heroe.vida+1
                    print heroe.vida
                if heroe.vida==0:
                    tema.play()
                n.velocidad=randint(1,5)
                
            if heroe.rect.colliderect(n.rect) and control==1:
                control=0
        
           
                
               
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(0,0))
        screen.blit(texto_puntos,(550,0))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__ == '__main__':
      game()
