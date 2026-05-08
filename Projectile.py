import pygame
import math


projectile_img = pygame.image.load("assets/Projectile.png")
projectile_img = pygame.transform.scale(projectile_img, (60, 20))


class Projectile:
    def __init__(self, x, y, angle, speed=20):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = math.radians(angle)
        self.x_speed = math.cos(self.angle) * self.speed
        self.y_speed = math.sin(self.angle) * self.speed
        self.image = pygame.transform.rotate(projectile_img, -angle)


    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))