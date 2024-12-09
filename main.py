import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

updatable, drawable, asteroids, shots = (
    pygame.sprite.Group(),
    pygame.sprite.Group(),
    pygame.sprite.Group(),
    pygame.sprite.Group(),
)

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)


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

        for d in drawable:
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.is_collison(player):
                print("Game over!")
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()
