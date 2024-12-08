import pygame

import constants
from player import Player


def main() -> None:
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

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

        pygame.display.flip()


if __name__ == "__main__":
    main()
