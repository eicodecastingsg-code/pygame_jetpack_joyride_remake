import pygame
from Player import Player
import random
from Projectile import Projectile
from Missile import Missile
from Explosion import Explosion
from Coin import Coin
from FloatingText import FloatingText
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jetpack Joyride Python Remake")


# Load images
background_image = pygame.image.load("assets/BackdropMain.png")


# Resize images
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


# create player clones
player1 = Player(100, 100)

clock = pygame.time.Clock()
projectiles = []
background_x = 0
scroll_speed = 3
font = pygame.font.Font("assets/PressStart2P.ttf", 24)
distance = 0
missiles = []
explosions = []
coins = []
coin_distance_counter = 0
coin_sound = pygame.mixer.Sound("assets/Coin.wav")
coin_sound.set_volume(0.5)
coin_count = 0
floating_text = []



def spawn_coin_array(startX, startY, rows, cols, spacing):
    for j in range(0, rows, 1):
        # build 1 row
        for i in range(0, cols, 1):
            x = startX + (i * spacing)
            y = startY + (j * spacing)
            coin_clone = Coin(x, y)
            coins.append(coin_clone)




def draw_health_bar(surface, current_health, max_health):
    width = 200
    height = 20
    x = 595
    y = 5

    # background
    pygame.draw.rect(surface, (70, 70, 70), (x, y, width, height))

    # fill
    health_ratio = current_health / max_health
    fill_length = health_ratio * width
    pygame.draw.rect(surface, (255, 0, 0), (x, y, fill_length, height))


    # Outline
    pygame.draw.rect(surface, (25, 255, 0), (x, y, width, height), 2)







# Main Game Loop
running = True
while running:

    background_x -= scroll_speed
    if background_x < -WIDTH:
        background_x = 0
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + WIDTH, 0))

    distance += scroll_speed - 2.9
    distance = round(distance, 3)


    # define winning and losing conditions
    if coin_count >= 100 and player1.current_health > 0:
        win_label = font.render("YOU WIN!!! ^_^", True, (0, 255, 0))
        screen.blit(win_label, (350, 300))
        pygame.display.flip()  # <-- this makes it show
        time.sleep(5)
        break


    if player1.current_health < 1:
        lose_label = font.render("YOU LOSE...T_T", True, (0, 255, 0))
        screen.blit(lose_label, (350, 300))
        pygame.display.flip()  # <-- this makes it show
        time.sleep(5)
        break



    # define key press event
    keys = pygame.key.get_pressed()

    if player1.fly(keys):
        angle = random.randint(70, 110)
        x, y = player1.x, player1.y
        projectile_clone = Projectile(x+10, y+20, angle)
        projectiles.append(projectile_clone)


    for clone in projectiles:
        clone.move()
        clone.draw(screen)
        if clone.x < 50 or clone.y > 500:
            projectiles.remove(clone)


    player1.update()
    player1.draw(screen)
    player_hitbox = player1.build_hitbox()


    # In each frame (in each game loop repetition),
    # 2% chance of creating a missile clone
    if random.randint(0, 100) < 1:
        missile_y = random.randint(50, HEIGHT - 50)
        missile_clone = Missile(WIDTH, missile_y, player1)
        missiles.append(missile_clone)

    for m in missiles:
        m.move()
        m.draw(screen)
        if m.x < -80:
            missiles.remove(m)
        if player_hitbox.colliderect(m.rect) and not player1.invincible:
            explosion_clone = Explosion(player1.x, player1.y)
            explosions.append(explosion_clone)
            player1.current_health -= 5
            player1.invincible = True
            player1.invincible_timer = 90 # 90 frames for 1.5s
            missiles.remove(m)


    # draw explosion clones
    for e in explosions:
        e.update()
        e.draw(screen)
        if e.finished:
            explosions.remove(e)


    coin_distance_counter += scroll_speed

    # 1 in 150 chance of spawning a coin array
    if random.randint(0, 150) == 0 and coin_distance_counter > 400:
        rows = random.randint(1, 5)
        cols = random.randint(1, 5)
        spawn_coin_array(900, random.randint(50, 350), rows, cols, 40)
        coin_distance_counter = 0

    for c in coins:
        c.draw(screen)
        c.move(scroll_speed)
        if c.check_collision(player_hitbox):
            coin_count += 1
            coin_sound.play()
            coins.remove(c)
            floating_text_clone = FloatingText(c.x, c.y)
            floating_text.append(floating_text_clone)
        if c.x < -30:
            coins.remove(c)


    for f in floating_text:
        f.update()
        f.draw(screen)
        if not f.is_alive():
            floating_text.remove(f)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Build text labels
    distance_label = font.render(f"Distance: {distance}m", True, (255, 255, 255))
    screen.blit(distance_label, (10, 5))

    coin_label = font.render(f"Coins: {coin_count}", True, (255, 255, 0))
    screen.blit(coin_label, (10, 30))

    draw_health_bar(screen, player1.current_health, player1.max_health)


    # refresh / update the game screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

























