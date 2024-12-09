import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

updatables, drawables, asteroids, shots = (
    pygame.sprite.Group(),
    pygame.sprite.Group(),
    pygame.sprite.Group(),
    pygame.sprite.Group(),
)

Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = (updatables,)
Shot.containers = (shots, updatables, drawables)


def main() -> None:
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:

        screen.fill("black")
        dt = clock.tick(240) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for drawable in drawables:
            drawable.draw(screen)

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collison(player):
                print("Game over!")
                return

            for shot in shots:
                if shot.is_collison(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()


if __name__ == "__main__":
    main()
