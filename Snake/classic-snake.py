import pygame
import random
import os

# Инциализация
pygame.init()
pygame.mixer.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')


# snake
snake_size = 15
snake_speed = 15
snake_x = random.randrange(0, width - snake_size, snake_speed)
snake_y = random.randrange(100, height - snake_size, snake_speed)
snake_body = []
snake_length = 5


snake_body.append([snake_x, snake_y])
for i in range(1, snake_length):
    snake_body.append([snake_x - i * snake_size, snake_y])

# colors
green = (0, 250, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
blue = (0, 0, 250)

# food
food_size = 15
food_x = random.randrange(0, width - food_size, snake_size)
food_y = random.randrange(100, height - food_size, snake_size)
food_rect = pygame.Rect(food_x, food_y, food_size, food_size)

def snake_draw():
    for snake_pos in snake_body:
        x, y = snake_pos[0], snake_pos[1]
        if x == snake_x and y == snake_y:
            color = blue
        else:
            color = green
        pygame.draw.rect(screen, color, (x, y, snake_size, snake_size))


direction = 'RIGHT'

# статистика
font = pygame.font.SysFont(None, 36)
apples = 0


def screen_text(text, color, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, y))

def write_text(text, color, x, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (x, y))

def start_screen():
    screen.fill(black)
    screen_text("Snake", green, height // 2 - 10)
    screen_text("За начало натисни бутона SPACE.", white, height // 2 + 20)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            waiting = False


def game_over_screen():
    screen.fill(black)
    screen_text("Ти загуби!", red, height // 2 - 10)
    screen_text(f"Твоят резултат е: {apples}", red, height // 2 + 20)
    screen_text("Натисни END за край.", red, height // 2 + 50)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_END]:
            waiting = False


start_screen()
clock = pygame.time.Clock()
running = True
while running:
    speed = min(15 + apples // 5, 30)
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
    snake_speed = snake_size
    if direction == 'LEFT':
        snake_x -= snake_speed
    elif direction == 'RIGHT':
        snake_x += snake_speed
    elif direction == 'UP':
        snake_y -= snake_speed
    elif direction == 'DOWN':
        snake_y += snake_speed

    if snake_x < 0 or snake_y < 0 or snake_x >= width or snake_y >= height:
        game_over_screen()
        running = False

    if [snake_x, snake_y] in snake_body[:-1]:
        game_over_screen()
        running = False

    snake_body.append([snake_x, snake_y])

    if len(snake_body) > snake_length:
        snake_body.pop(0)

    snake_head = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
    if snake_head.colliderect(food_rect):
        snake_length += 1
        apples += 1
        food_x = random.randrange(0, width - food_size, snake_size)
        food_y = random.randrange(100, height - food_size, snake_size)
        food_rect = pygame.Rect(food_x, food_y, food_size, food_size)

    # Рисуваме
    screen.fill(white)
    snake_draw()
    pygame.draw.rect(screen, red, food_rect)
    text_1 = font.render(f"Изядени ябълки: {apples}", True, black)
    screen.blit(text_1, (10, 10))
    pygame.display.flip()

pygame.quit()
