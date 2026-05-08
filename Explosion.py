import pygame

class Explosion:
    def __init__(self, x, y):
        self.costume_list = []

        for i in range(2, 19, 1):
            image = pygame.image.load(f"assets/explosion/Untitled{i}.png")
            image = pygame.transform.scale(image, (60, 60))
            self.costume_list.append(image)

        self.costume_num = 0
        self.x = x
        self.y = y
        self.costume = self.costume_list[self.costume_num]
        self.finished = False   # has an explosion clone finished exploding?


    def update(self):
        self.costume_num += 1
        if self.costume_num >= 17:
            self.finished = True


    def draw(self, screen):
        if not self.finished:
            self.costume = self.costume_list[self.costume_num]
            rect = self.costume.get_rect(center=(self.x, self.y))
            screen.blit(self.costume, rect.center)

    



















