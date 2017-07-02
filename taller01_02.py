import sys, pygame

size = width, height = 640, 400
speed = [1, 1]
screen = pygame.display.set_mode(size)

def main():
        pygame.init()
        ball = pygame.image.load("imagenes/basketball.png")
        ballrect = ball.get_rect()
        ballrect.left = (width/2)-(ballrect.width/2)
        ballrect.top = (height/2)-(ballrect.height/2)

        court = pygame.image.load("imagenes/cancha.png")
        courtrect = court.get_rect()

        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                ballrect = ballrect.move(speed)
                if ballrect.top < height-height or ballrect.bottom > height:
                
                    speed[1] = -speed[1]
                if  ballrect.left < width-width or ballrect.right > width :
                    speed[0] = -speed[0]
                screen.blit(court, courtrect)
                screen.blit(ball, ballrect)

                pygame.display.update()

if __name__ == '__main__':
 main()
