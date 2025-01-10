import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            random_angle = random.uniform(20, 50)
            random_angle_pos = self.velocity.rotate(random_angle)
            random_angle_neg = self.velocity.rotate(-random_angle)

            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(
                self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(
                self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = random_angle_pos * 1.2
            asteroid_two.velocity = random_angle_neg * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
