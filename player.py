import pygame
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # move left
        if keys[pygame.K_LEFT]:
            new_dt = -dt
            self.rotate(new_dt)

        # move right
        if keys[pygame.K_RIGHT]:
            new_dt = dt
            self.rotate(new_dt)

        # move upward
        if keys[pygame.K_UP]:
            self.move(dt)

        # move downward
        if keys[pygame.K_DOWN]:
            self.move(dt)

        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED
