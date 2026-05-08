import pygame
import math
import random
from Smoke import SmokeParticle

missile_img = pygame.image.load("assets/Missile.png")
missile_img = pygame.transform.scale(missile_img, (80, 60))
missile_img = pygame.transform.flip(missile_img, True, False)


class Missile:
    def __init__(self, x, y, target, speed=10):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = missile_img
        self.target = target
        self.homing_time = 30 # frames
        self.dx = 0
        self.dy = 0
        self.angle = 180 # missiles face left
        self.smoke_particles = []
        self.rect = self.image.get_rect(center=(self.x, self.y))


    def move(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))

        if self.homing_time > 0:
            # track the player for 1 frame
            diff_x = self.target.x - self.x
            diff_y = self.target.y - self.y
            angle_to_player = math.atan2(diff_y, diff_x)

            self.dx = math.cos(angle_to_player) * self.speed
            self.dy = math.sin(angle_to_player) * self.speed

            self.homing_time -= 1

        self.x += self.dx
        self.y += self.dy

        # Rotate missile image to point towards player
        self.angle = math.degrees(math.atan2(self.dy, self.dx))
        self.image = pygame.transform.rotate(missile_img, -self.angle)

        # Add smoke particles
        # 33.33% chance of spawning a smoke clone
        if random.randint(0, 2) == 0:
            smoke_clone = SmokeParticle(self.x + 60, self.y + 40)
            self.smoke_particles.append(smoke_clone)

        # update smoke
        for s in self.smoke_particles:
            s.update()
            if s.lifetime < 1:
                self.smoke_particles.remove(s)


    def draw(self, screen):
        # draw smoke
        for s in self.smoke_particles:
            s.draw(screen)

        screen.blit(self.image, (self.x, self.y))








































