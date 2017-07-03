import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *
from bono import *
from bonoInmune import *

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
    villano = [Villano((100,80),randint(1,10)),
               Villano((100,150),randint(1,10)),
               Villano((200,220),randint(1,10)),
               Villano((300,300),randint(1,10)),
               Villano((100,350),randint(1,10))]
    bonos = [Bono((randint(50,600),80),0),
               Bono((randint(50,600),150),0),
               Bono((randint(50,600),220),0),
               Bono((randint(50,600),300),0),
               Bono((randint(50,600),350),0)]
    bonosInmunes = [BonoInmune((randint(50,600),randint(50,400)),0),
             BonoInmune((randint(50,600),randint(50,400)),0)]
    m = villano[1]
    tinicio = pygame.time.get_ticks()
    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,0,0))
        texto_tiempo = fuente.render("Tiempo: 0",1,(0,0,0))
        if heroe.estado == "inmune":
            texto_tiempo = fuente.render("Tiempo: "+str(pygame.time.get_ticks()-tinicio),1,(0,0,0))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,0,0))
        
        heroe.update()
        for n in villano:
            n.update()

        for b in bonos:
            b.update()

        for bi in bonosInmunes:
            bi.update()

        for n in villano:
            if heroe.rect.colliderect(n.rect) and n != m:
                m=n
                if heroe.estado != "inmune":
                    heroe.image = heroe.imagenes[1]
                    pierde_vida.play()
                    if heroe.vida > 0:
                        heroe.vida=heroe.vida-1
                        n.velocidad=randint(1,10)
                else:
                    villano.remove(n)
            elif heroe.rect.colliderect(n.rect) and n == m:
                if heroe.estado != "inmune":
                    heroe.image = heroe.imagenes[1]
                else:
                    villano.remove(n)
                '''print 'colision antigua' '''
            elif heroe.rect.colliderect(n.rect) == False and n == m:
                m = None
                '''print 'sin colision' '''

        for b in bonos:
            if heroe.rect.colliderect(b.rect):
                if heroe.estado != "inmune":
                    heroe.image = heroe.imagenes[1]
                    if heroe.vida < 100:
                        heroe.vida=heroe.vida+2
                        bonos.remove(b)

        for bi in bonosInmunes:
            if heroe.rect.colliderect(bi.rect) and heroe.estado != "inmune":
                heroe.actInmunidad()
                heroe.image = heroe.imagenes[4]
                heroe.vida=100
                tinicio = pygame.time.get_ticks()
                bonosInmunes.remove(bi)

        if heroe.estado == "inmune":
            if (pygame.time.get_ticks()-tinicio) >= 60000:
                heroe.estado = "bajando"
                heroe.image = heroe.imagenes[4]
        if len(villano) < 5 and heroe.estado != "inmune":
                for n in villano:
                    villano.remove(n)
                villano = [Villano((100,80),randint(1,10)),
                           Villano((100,150),randint(1,10)),
                           Villano((200,220),randint(1,10)),
                           Villano((300,300),randint(1,10)),
                           Villano((100,350),randint(1,10))]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,450))
        screen.blit(texto_tiempo,(250,450))
        screen.blit(texto_puntos,(100,450))
        for n in villano:
            screen.blit(n.image, n.rect)
        for b in bonos:
            screen.blit(b.image, b.rect)
        for bi in bonosInmunes:
            screen.blit(bi.image, bi.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__ == '__main__':
      game()
