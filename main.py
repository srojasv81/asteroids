import pygame
from constants import *
from player import *

def main():
    # chapter 2 exercise 3
    pygame.init()
    reloj = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for player in updatable:
            player.update(dt)

        for player in drawable:
            player.draw(screen)
        
        pygame.display.flip()
        dt = reloj.tick(60) / 1000
        

if __name__ == "__main__":
    main()
