import pygame

coin_img = pygame.image.load("assets/Coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = coin_img
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, (self.x, self.y))

    def move(self, speed):
        self.x -= speed
        self.rect.x = self.x

    def check_collision(self, player_hitbox):
        if not self.collected and self.rect.colliderect(player_hitbox):
            self.collected = True
            return True
        return False
