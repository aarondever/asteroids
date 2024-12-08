import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
