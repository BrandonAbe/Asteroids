# Imports
import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")

    # Initialize the pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Create container properties for objects
    Player.containers = (updatable, drawable) # Enable each Player to be updatable, drawable
    Asteroid.containers = (asteroids, updatable, drawable) # Enable each Asteroid to be grouped together
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    '''
    Note: Adding the Player.containers allows any new Player to be added to the groups in the tuple passed
    in the containers argument. This means you do not need to manually call updatable.add(player)
    and drawable.add(player). This is convenient because it reduces code repitition, and ensures
    consistency (you can't forget to add a Player to a group)
    '''

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0 # Delta time

    # Create game loopdd
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the event is a quit event
                pygame.quit()

        updatable.update(dt) #updates entire group


        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision_detection(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill('black')

        for obj in drawable: # for every object that needs to be drawn...
            obj.draw(screen) # draw to screen
        

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0


if __name__ == "__main__":
    main()
