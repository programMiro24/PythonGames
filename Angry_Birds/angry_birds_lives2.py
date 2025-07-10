import pygame
import math
import os
import random


# Инциализация на pygame
pygame.init()
pygame.mixer.init()

# Прозореца
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Angry Birds - Lives")
background_color = (0, 0, 0)  # черно
text_color = (255, 255, 255)  # бяло

if os.path.exists("background.png"):
    background = pygame.image.load("background.png")
else:
    background = None
    print("ВНИМАНИЕ! Изображението background.png не може да бъде зареден.")

# Функция за текст
def draw_screen_text(text, color, y):
    title_text = font.render(text, True, color)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, y))

def space_escape():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            waiting = False

def start_screen():
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(background_color)

    draw_screen_text("Angry Birds", text_color, height // 2 - 30)
    draw_screen_text("Натисни SPACE за старт.", text_color, height // 2)
    pygame.display.flip()
    space_escape()

def level_screen(level, seconds):
    screen.fill(black)
    draw_screen_text(f"Ти премина на ниво {level}!", white, height // 2 - 50)
    draw_screen_text(f"Ще имаш {seconds} секунди, за да застреляш прасетата.", white, height // 2 - 20)
    draw_screen_text("Ако не успееш навреме, ще загубиш точки.", white, height // 2 + 10)
    draw_screen_text("Натисни SPACE, за да продължиш.", white, height // 2 + 40)
    pygame.display.flip()
    space_escape()

def game_over_screen():
    screen.fill(black)
    draw_screen_text("Край на играта.", white, height // 2 - 50)
    draw_screen_text(f"Ти успя да застреляш {hits} пъти различните прасета.", white, height // 2 - 20)
    draw_screen_text("Натисни END за край.", red, height // 2 + 10)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_END]:
            waiting = False

# Цветове
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
black = (0, 0, 0)
yellow = (255, 200, 0)

# Позиция на прашкатаа
sligshot_x, sligshot_y = 150, height - 200


# Състояние
dragging = False
bird_png = pygame.image.load('angry-birds.png')
bird_pos = [sligshot_x, sligshot_y]
bird_velocity = [0, 0]
bird_radius = 32
gravity = 0.5
launced = False
launcher_timer = 0

# Мишена


class Target:
    def __init__(self, x, y, w=64, h=64, health=3):
        self.rect = pygame.Rect(x, y, w, h)
        self.max_health = health
        self.health = health
        self.alive = True
        self.img = pygame.image.load('piggy.png')

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def draw(self, screen):
        if not self.alive:
            return
        if self.health == 3:
            self.img = pygame.image.load('piggy.png')
        elif self.health == 2:
            self.img = pygame.image.load('pig2.png')
        else:
            self.img = pygame.image.load('pig3.png')

        screen.blit(self.img, (self.rect.x, self.rect.y))


target = Target(random.randint(400, 800 - 40), random.randint(0, height - 120))

# статистика
shots_fired = 0
hits = 0
points = 0
shooter = 0
shooter_timer = 0
level = 1

# Шрифт
font = pygame.font.SysFont(None, 32)

# Зареждане на звук
if os.path.exists("hit.wav"):
    hit_sound = pygame.mixer.Sound("hit.wav")
else:
    hit_sound = None
    print("ВНИМАНИЕ! Звукът hit.wav не може да бъде зареден.")

start_screen()
previous_level = 1
dx=dy=-1
clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # започваш дърпането
            if not launced:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = math.hypot(mouse_x - bird_pos[0], mouse_y - bird_pos[1])
                if distance <= bird_radius:
                    dragging = True

        # пускане на птицата
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False
                launced = True
                launcher_timer = 0
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = sligshot_x - mouse_x
                dy = sligshot_y - mouse_y
                bird_velocity = [dx * 0.2, dy * 0.2]
                shots_fired += 1  # Нов изстрел

        # Обработка на рестарт след удар
        elif event.type == pygame.USEREVENT:
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            pygame.time.set_timer(pygame.USEREVENT, 0)
            if not target.alive:
                target = Target(random.randint(400, 760), random.randint(0, height - 120))
                shooter_timer = 0
                shooter = 0

    shooter_timer += dt
    # ако дърпаш птицата
    if dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        bird_pos[0] = mouse_x
        bird_pos[1] = mouse_y

    # ако си я изстрелял
    elif launced:
        bird_velocity[1] += gravity
        bird_pos[0] += bird_velocity[0]
        bird_pos[1] += bird_velocity[1]
        launcher_timer += dt
        if launcher_timer > 1000: # or bird_pos[0] > width or bird_pos[1] > height:
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            target_hit = False  # нова цел
    if level == 1 and hits == 9:
        level += 1
        level_screen(level, 10)


    # Проверка за сблъсък с мишената
    if target.alive:
        bird_rect = pygame.Rect(bird_pos[0] - bird_radius, bird_pos[1] - bird_radius, bird_radius * 2,
        bird_radius * 2)
        if bird_rect.colliderect(target.rect):
            target.hit()
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            hits += 1
            shooter += 1
            if hit_sound:
                hit_sound.play()
            # Рестартиране след 1 секунда
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            if hits <= 9:
                points += 5
            elif shooter == 3:
                points += shooter * 10

        if shooter_timer > 10_000 and shooter < 3 and hits >= 9:
            points -= (3 - shooter) * 10
            target.alive = False
            pygame.time.set_timer(pygame.USEREVENT, 1000)

    if points <= 0 and level != 1:
        game_over_screen()
        running = False

    # Рисуване
    screen.blit(bird_png, (bird_pos[0] - bird_radius, bird_pos[1] - bird_radius))
    pygame.draw.line(screen, black, (sligshot_x, sligshot_y), (int(bird_pos[0]), int(bird_pos[1])), 2)
    pygame.draw.circle(screen, black, (sligshot_x, sligshot_y), 5)

    target.draw(screen)

    # Статистика
    text1 = font.render(f'Изстрели: {shots_fired}', True, black)
    text2 = font.render(f'Удари: {hits}', True, black)
    text3 = font.render(f'Точки: {points}', True, black)
    text4 = font.render(f'Време: {10 - (shooter_timer // 1000)}', True, black)
    text5 = font.render(f'Ниво: {level}', True, black)
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    if level > 1:
        screen.blit(text4, (10, 100))
        screen.blit(text5, (10, 130))
    else:
        screen.blit(text5, (10, 100))


    pygame.display.update()


pygame.quit()


