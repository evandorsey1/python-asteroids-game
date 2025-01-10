import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

             # Update dt first
            for object in updatable:
                object.update(dt)

            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    print("Game over!")
                    exit()

            # Fill screen
            screen.fill((0, 0, 0))

            # Draw screen
            for object in drawable:
                object.draw(screen)

            # Update the full display Surface to the screen
            pygame.display.flip()

            # Limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
