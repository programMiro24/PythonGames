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
snake_length = 10


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
            if snake_img:
                screen.blit(snake_img, (x, y))
                continue
            else:
                color = blue
        else:
            color = green
        pygame.draw.rect(screen, color, (x, y, snake_size, snake_size))


direction = 'RIGHT'

# статистика
font = pygame.font.SysFont(None, 36)
apples = 0

# зареждане на файлове
if os.path.exists("background.png"):
    background_img = pygame.image.load("background.png")
else:
    background_img = None
    print("Изображението background.png не може да бъде зареден.")

if os.path.exists("food.png"):
    food_img = pygame.image.load("food.png")
else:
    food_img = None
    print("Изображението food.png не може да бъде зареден.")

if os.path.exists("snake.png"):
    snake_img = pygame.image.load("snake.png")
else:
    snake_img = None
    print("Изображението snake.png не може да бъде зареден.")

if os.path.exists("food.wav"):
    food_sound = pygame.mixer.Sound("food.wav")
else:
    food_sound = None
    print("Звукът food.wav не може да бъде зареден.")

if os.path.exists("background_music.wav"):
    background_music = pygame.mixer.Sound("background_music.wav")
else:
    background_music = None
    print("Звукът background_music.wav не може да бъде зареден.")

if os.path.exists("apple_boostsize.png"):
    apple_boostsize = pygame.image.load("apple_boostsize.png")
else:
    apple_boostsize = None
    print("Изображението apple_boostsize.png не може да бъде зареден.")

def screen_text(text, color, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, y))

def write_text(text, color, x, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (x, y))

def start_screen():
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
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
    if background_music:
        background_music.stop()
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

if background_music:
    background_music.play(loops=-1)

start_screen()
timer = 0
clock = pygame.time.Clock()
running = True
while running:
    fps_speed = min(15 + apples // 5, 35)
    dt = clock.tick(fps_speed)
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

    timer += dt

    snake_speed = snake_size
    # prev_x, prev_y = snake_x, snake_y
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
        if food_sound:
            food_sound.play()
        food_x = random.randrange(0, width - food_size, snake_size)
        food_y = random.randrange(100, height - food_size, snake_size)
        food_rect = pygame.Rect(food_x, food_y, food_size, food_size)

    # Рисуваме
    screen.fill(white)

    snake_draw()
    if food_img:
        screen.blit(food_img, (food_rect.x, food_rect.y))
    else:
        pygame.draw.rect(screen, red, food_rect)
    text_1 = font.render(f"Изядени ябълки: {apples}", True, black)
    seconds = timer // 1_000
    minutes = seconds // 60
    seconds %= 60
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'
    text_2 = font.render(f"Време: {minutes}:{seconds}", True, black)
    level = apples // 5 + 1
    text_3 = font.render(f"Ниво: {level}", True, black)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (10, 40))
    screen.blit(text_3, (10, 70))
    pygame.display.flip()

pygame.quit()

"""
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and direction != 'RIGHT': #and snake_x > 0:
    snake_x -= snake_speed
    direction = 'LEFT'
elif keys[pygame.K_RIGHT] and direction != 'LEFT': #and snake_x < width - snake_size:
    snake_x += snake_speed
    direction = 'RIGHT'
elif keys[pygame.K_UP] and direction != 'DOWN': #and snake_y > 0:
    snake_y -= snake_speed
    direction = 'UP'
elif keys[pygame.K_DOWN] and direction != 'UP': #and snake_y < height - snake_size:
    snake_y += snake_speed
    direction = 'DOWN'
"""
