import random

import pygame

import constants
from circleshape import CircleShape


class Asteroid(CircleShape):

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        self.velocity.rotate(random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        for i in (1, -1):
            Asteroid(self.position.x, self.position.y, new_radius).velocity = (
                self.velocity.rotate(random_angle * i)
                * constants.ASTEROID_SPEED_SCALER_AFTER_SPLIT
            )
