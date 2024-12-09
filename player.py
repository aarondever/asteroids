import pygame

import constants
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_cd_timer = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def roate(self, dt: float) -> None:
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.roate(-dt)

        if keys[pygame.K_d]:
            self.roate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.shot_cd_timer <= 0:
            self.shoot()
            self.shot_cd_timer = constants.PLAYER_SHOOT_COOLDOWN

        if self.shot_cd_timer > 0:
            self.shot_cd_timer -= dt

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        )
