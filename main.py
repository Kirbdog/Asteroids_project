from constants import *
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
