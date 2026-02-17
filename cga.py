import pygame
import random
import math

# Initialize
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Escape: Retro Rocket")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Colors
WHITE = (240, 240, 240)
RED = (220, 60, 60)
YELLOW = (255, 255, 0)
BLUE = (120, 200, 210)
BLACK = (0, 0, 0)
GREEN = (120, 255, 180)
ORANGE = (255, 140, 0)

# Player (Rocket)
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 6
bullets = []

# Enemies
enemies = []
enemy_timer = 0

# Stars
stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(80)]

score = 0
game_over = False


def draw_rocket(x, y):
    # 🔺 Nose cone
    pygame.draw.polygon(
        screen, RED,
        [(x, y - 15), (x - 8, y), (x + 8, y)]
    )

    # 🚀 Body
    pygame.draw.rect(
        screen, BLUE,
        (x - 8, y, 16, 35)
    )

    # 🪟 Window
    pygame.draw.circle(screen, WHITE, (x, y + 12), 5)
    pygame.draw.circle(screen, GREEN, (x, y + 12), 3)

    # 🔺 Left fin
    pygame.draw.polygon(
        screen, RED,
        [(x - 8, y + 20), (x - 15, y + 32), (x - 8, y + 32)]
    )

    # 🔺 Right fin
    pygame.draw.polygon(
        screen, RED,
        [(x + 8, y + 20), (x + 15, y + 32), (x + 8, y + 32)]
    )

    # 🔥 Flame
    pygame.draw.polygon(
        screen, ORANGE,
        [(x - 5, y + 35), (x, y + 48), (x + 5, y + 35)]
    )


def draw_enemy(x, y):
    pygame.draw.circle(screen, RED, (x, y), 15)
    pygame.draw.line(screen, YELLOW, (x - 10, y), (x + 10, y), 2)


def draw_stars():
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)
        star[1] += 2
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0


def collision(x1, y1, x2, y2, dist):
    return math.hypot(x1 - x2, y1 - y2) < dist


running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)
    draw_stars()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x, player_y])

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > 20:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 20:
            player_x += player_speed

    # Draw Player
    if not game_over:
        draw_rocket(player_x, player_y)

    # Bullets
    for bullet in bullets[:]:
        bullet[1] -= 10
        pygame.draw.rect(screen, YELLOW, (bullet[0] - 2, bullet[1], 4, 10))
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn Enemies
    enemy_timer += 1
    if enemy_timer > 40:
        enemies.append([random.randint(30, WIDTH - 30), 0, random.randint(2, 5)])
        enemy_timer = 0

    # Enemy Movement
    for enemy in enemies[:]:
        enemy[1] += enemy[2]
        draw_enemy(enemy[0], enemy[1])

        # Player Collision (adjusted center slightly down)
        if collision(player_x, player_y + 20, enemy[0], enemy[1], 30):
            game_over = True

        # Bullet Collision
        for bullet in bullets[:]:
            if collision(bullet[0], bullet[1], enemy[0], enemy[1], 20):
                if enemy in enemies:
                    enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 10

        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            score += 1

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game Over
    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, RED)
        screen.blit(over_text, (WIDTH // 2 - 170, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            enemies.clear()
            bullets.clear()
            score = 0
            game_over = False

    pygame.display.update()

pygame.quit()
