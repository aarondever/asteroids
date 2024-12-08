from typing import Self

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: float) -> None:
        # sub-classes must override
        pass

    def is_collison(self, circle: Self) -> bool:
        return self.position.distance_to(circle.position) < self.radius + circle.radius
