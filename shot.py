import pygame
from pygame import Surface

import constants
from circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
