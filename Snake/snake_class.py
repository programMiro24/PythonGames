import pygame
import random
import os
import sys

# Инциализация
pygame.init()
pygame.mixer.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# colors
green = (0, 250, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
blue = (0, 0, 250)
yellow = (200, 200, 0)

# snake

class Snake:
    def __init__(self, x, y, color1=green, color2=blue, size=15, length=10, direction='RIGHT', points = 0):
        self.size = size
        self.speed = self.size
        self.x = x  # random.randrange(0, width - snake_size, snake_speed)
        self.y = y  # random.randrange(100, height - snake_size, snake_speed)
        self.body = []
        self.length = length
        self.direction = direction
        self.head = None
        self.points = points
        self.color1 = color1
        self.color2 = color2
        self.color = None

    def init_body(self):
        self.body.append([self.x, self.y])
        for i in range(1, self.length):
            self.body.append([self.x - i * self.size, self.y])

    def move(self):
        self.speed = self.size
        if self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed
        elif self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed

    def snake_draw(self):
        for snake_pos in self.body:
            x, y = snake_pos[0], snake_pos[1]
            if x == self.x and y == self.y:
                if snake_img:
                    screen.blit(snake_img, (x, y))
                    continue
                else:
                    self.color = self.color2
            else:
                self.color = self.color1
            pygame.draw.rect(screen, self.color, (x, y, self.size, self.size))

    def is_dead(self):
        if self.x < 0 or self.y < 0 or self.x >= width or self.y >= height:
            return True  # ударил се е в стена
        if [self.x, self.y] in self.body[:-1]:
            return True
        return False

    def update_snake_body(self):
        self.body.append([snake.x, snake.y])

        if len(self.body) > self.length:
            self.body.pop(0)

        self.head = pygame.Rect(self.x, self.y, self.size, self.size)

class Food:
    def __init__(self, snake_body, size=15, apple_type=-1, apples=0):
        self.apple_type = apple_type
        self.apples = apples
        self.size = size
        self.food_img = None
        self.apple_boostsize = None
        self.apple_points = None
        self.x = 0
        self.y = 0
        self.rect = None
        self.update(snake_body)

    def update(self, snake_body):
        self.apple_type = random.choices([0, 1, 2], weights=[70, 25, 5])[0]
        # 0 - нормална(червена), 1 - увеличаваща дължина(зелена), 2 - увеличава точките * 2(златна)
        while True:
            self.x = random.randrange(0, width - self.size, snake.size)
            self.y = random.randrange(130, height - self.size, snake.size)
            if [self.x, self.y] not in snake_body:
                break
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, food_img, apple_boostsize, apple_points):
        self.food_img = food_img
        self.apple_boostsize = apple_boostsize
        self.apple_points = apple_points
        if self.apple_type == 0:
            if self.food_img:
                screen.blit(self.food_img, (self.rect.x, self.rect.y))
            else:
                pygame.draw.rect(screen, red, self.rect)
        elif self.apple_type == 1:
            if self.apple_boostsize:
                screen.blit(apple_boostsize, (self.rect.x, self.rect.y))
            else:
                pygame.draw.rect(screen, green, self.rect)
        else:
            if self.apple_points:
                screen.blit(self.apple_points, (self.rect.x, self.rect.y))
            else:
                pygame.draw.rect(screen, yellow, self.rect)


# snake
snake = Snake(random.randrange(0, width - 15, 15), random.randrange(100, height - 15, 15))

snake.init_body()

# food
food = Food(snake.body)


# статистика
font = pygame.font.SysFont(None, 36)


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

if os.path.exists("apple_points.png"):
    apple_points = pygame.image.load("apple_points.png")
else:
    apple_points = None
    print("ВНИМАНИЕ! Изображението apple_points.png не може да бъде заредено.")

def screen_text(text, color, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, y))

def start_screen():
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(black)
    screen_text("Snake", green, height // 2 - 30)
    screen_text("За начало натисни бутона SPACE.", white, height // 2 + 0)
    screen_text("Указания:", white, height // 2 + 50)

    # apple_type == 2
    if apple_points:
        screen.blit(apple_points, (width // 2 - apple_points.get_width() // 2 - 355, height // 2 + 85))
    else:
        pygame.draw.rect(screen, yellow, food.rect)
    screen_text("Златната ябълка ви дава 40 точки, но ви забавя за 5 сек.", white, height // 2 + 80)

    # apple_type == 1
    if apple_boostsize:
        screen.blit(apple_boostsize, (width // 2 - apple_points.get_width() // 2 - 375, height // 2 + 115))
    else:
        pygame.draw.rect(screen, yellow, food.rect)
    screen_text("Зелената ябълка ви дава 20 точки, но ви забързва за 5 сек.", white, height // 2 + 110)

    # apple_type == 0
    if food_img:
        screen.blit(food_img, (width // 2 - apple_points.get_width() // 2 - 335, height // 2 + 145))
    else:
        pygame.draw.rect(screen, yellow, food.rect)
    screen_text("Червената ябълка ви дава 10 точки. Тя е нормална.", white, height // 2 + 140)

    pygame.display.update()
    pygame.time.delay(30)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def game_over_screen():
    if background_music:
        background_music.stop()
    screen.fill(black)
    screen_text("Ти загуби!", red, height // 2 - 10)
    screen_text(f"Твоят резултат е: {food.apples}", red, height // 2 + 20)
    screen_text(f"Твоите точки са: {snake.points}", red, height // 2 + 50)
    screen_text("Натисни END за край или R за рестарт.", red, height // 2 + 80)

    pygame.display.update()

    waiting = True
    restart = False
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_END]:
            waiting = False
        elif keys[pygame.K_r]:
            waiting = False
            restart = True
    return restart

def restart():
    global snake, food, timer, is_slow, is_boosted
    # snake
    snake = Snake(random.randrange(0, width - 15, 15), random.randrange(100, height - 15, 15))
    snake.init_body()
    # food
    food = Food(snake.body)
    # timer
    timer = 0
    # FPS
    is_slow = False
    is_boosted = False
    # restart music
    if background_music:
        background_music.stop()
        background_music.play(loops=-1)

def pause_screen():
    screen.fill(black)
    screen_text("Меню за пауза", white, height // 2)
    screen_text("Натисни P за продължаване.", white, height // 2 + 30)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False

start_screen()
timer = 0

# FPS
clock = pygame.time.Clock()
start_fps = 15

is_boosted = False
boosted_limit_time = 5000 # 5 sec boost
speed_boost_start_time = 0
boosted_fps = 30

slow_fps = 8
is_slow = False
slow_limit_time = 5000 # 5 sec slow
speed_slow_time = 0

if background_music:
    background_music.play(loops=-1)

running = True
while running:
    current_time = pygame.time.get_ticks()
    if is_boosted:
        if current_time - speed_boost_start_time < boosted_limit_time:
            fps_speed = boosted_fps
        else:
            is_boosted = False
            fps_speed = min(start_fps + food.apples // 5, 25)
    elif is_slow:
        if current_time - speed_slow_time < slow_limit_time:
            fps_speed = slow_fps
        else:
            is_slow = False
            fps_speed = min(start_fps + food.apples // 5, 25)
    else:
        fps_speed = min(start_fps + food.apples // 5, 25)
    dt = clock.tick(fps_speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'
            elif event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_p:
                pause_screen()

    timer += dt
    snake.move()
    if snake.is_dead():
        if not game_over_screen():
            running = False
        else:
            restart()

    snake.update_snake_body()
    if snake.head.colliderect(food.rect):
        if food.apple_type == 0:
            snake.points += 5
            snake.length += 1
        elif food.apple_type == 1:
            snake.length += 2
            snake.points += 10
            if not is_boosted:
                is_boosted = True
                speed_boost_start_time = pygame.time.get_ticks()
            else:
                boosted_limit_time = min(20000, boosted_limit_time + 5000)
        else:
            snake.points += 40
            snake.length += 5
            is_slow = True
            speed_slow_time = pygame.time.get_ticks()

        food.apples += 1
        if food_sound:
            food_sound.play()
        food.update(snake.body)

    # Рисуваме
    screen.fill(white)

    snake.snake_draw()

    food.draw(food_img, apple_boostsize, apple_points)
    text_1 = font.render(f"Изядени ябълки: {food.apples}", True, black)
    seconds = timer // 1000
    minutes = seconds // 60
    seconds %= 60
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'
    text_2 = font.render(f"Време: {minutes}:{seconds}", True, black)
    level = food.apples // 5 + 1
    text_3 = font.render(f"Ниво: {level}", True, black)
    text_4 = font.render(f"Точки: {snake.points}", True, black)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (10, 40))
    screen.blit(text_3, (10, 70))
    screen.blit(text_4, (10, 100))
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
