import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    #main code
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        black = (0, 0, 0)
        screen.fill(black)
        player.draw(screen)
        pygame.display.flip()
       
        #limit framerate to 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
