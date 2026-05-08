import pygame
import random

class SmokeParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(10, 15)
        self.lifetime = 25 # a smoke particle lasts 25 frames
        self.color = (255, 0, 0)

    def update(self):
        self.size -= random.randint(0, 1)
        self.lifetime -= 1
        self.x -= 1 # drift left

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))
