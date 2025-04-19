# Imports
import pygame
from constants import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time

    # Create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the event is a quit event
                pygame.quit()
                sys.exit()

        screen.fill('black')
        pygame.display.flip()
        clock.tick(FPS)
        dt = clock.get_time() / 1000.0


if __name__ == "__main__":
    main()
