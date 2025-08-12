from constants import *
import pygame
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
