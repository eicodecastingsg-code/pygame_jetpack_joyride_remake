import pygame

class Player:
    # constructor function
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_index = 0
        self.gravity = 0.3
        self.y_speed = 0
        self.jetpack_power = -0.8
        self.walking = True
        self.anim_counter = 0
        self.anim_cooldown = 5
        self.max_health = 100
        self.current_health = self.max_health
        self.invincible = False
        self.invincible_timer = 0


        self.walk_images = [
            pygame.image.load("assets/Walk1.png"),
            pygame.image.load("assets/Walk2.png"),
            pygame.image.load("assets/Walk3.png"),
        ]
        self.fly_image = pygame.image.load("assets/Fly.png")
        self.death_image = pygame.image.load("assets/Death.png")

        self.image = self.walk_images[self.image_index]


    def fly(self, keys):
        if keys[pygame.K_SPACE]:
            self.y_speed += self.jetpack_power
            self.walking = False
            return True
        else:
            self.walking = True
        return False


    def update(self):
        # Gravity
        self.y_speed += self.gravity
        self.y += self.y_speed

        # Set bound and clamp the player
        if self.y > 460:
            self.y = 460
            self.y_speed = 0
        elif self.y < 70:
            self.y = 70
            self.y_speed = 0


        # Animation
        self.anim_counter += 1
        if self.walking:
            if self.anim_counter > self.anim_cooldown:
                self.image_index += 1
                if self.image_index > 2:
                    self.image_index = 0
                self.image = self.walk_images[self.image_index]
                self.anim_counter = 0
        else:
            self.image = self.fly_image

        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False


    def draw(self, screen):
        # skip painting player's image if it's an even frame
        if self.invincible and (pygame.time.get_ticks() // 100) % 2 == 0:
            return

        screen.blit(self.image, (self.x, self.y))

    # build a function that returns player's hitbox
    def build_hitbox(self):
        return pygame.Rect(self.x, self.y, 40, 40)
























