import pygame

def cargar_imagen(nombre, optimizar=False):
    imagen = pygame.image.load(nombre)

    if optimizar:
        return imagen.convert()
    else:
        return imagen.convert_alpha()

def cargar_sonido(nombre):
        return pygame.mixer.Sound(nombre)

               
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,450))
        screen.blit(texto_podercerveza,(400,450))
        screen.blit(texto_puntos,(100,450))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__ == '__main__':
      game()
