# Imports
import pygame
from constants import *
from player import Player
from circleshape import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # Set both groups as containers for the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0 # Delta time

    # Create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the event is a quit event
                pygame.quit()

        updatable.update(dt) #updates entire group
        screen.fill('black')

        for obj in drawable: # for every object that needs to be drawn...
            obj.draw(screen) # draw to screen

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0


if __name__ == "__main__":
    main()
