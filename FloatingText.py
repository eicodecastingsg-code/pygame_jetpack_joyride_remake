import pygame

class FloatingText:
    def __init__(self, x, y, text="+1", color=(255, 255, 0), lifespan=30):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.lifespan = lifespan
        self.alpha = 255
        self.font = pygame.font.Font("assets/PressStart2P.ttf", 100)  # Use your pixel font

    def update(self):
        self.y -= 1  # Float upward
        self.lifespan -= 1
        if self.alpha > 0:
            self.alpha -= 10  # Fade out

    def draw(self, screen):
        if self.lifespan > 0:
            text_surface = self.font.render(self.text, True, self.color)
            text_surface.set_alpha(self.alpha)
            screen.blit(text_surface, (self.x, self.y))

    def is_alive(self):
        return self.lifespan > 0