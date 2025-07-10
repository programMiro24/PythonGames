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

# Цветове
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
black = (0, 0, 0)
yellow = (255, 200, 0)
# Позиция на прашкатаа
sligshot_x, sligshot_y = 150, height - 100


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
    def __init__(self, x, y, w = 40, h = 40, health = 3):
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

target = Target(random.randint(400, 760), random.randint(0, height - 120))

# статистика
shots_fired = 0
hits = 0

# Шрифт
font = pygame.font.SysFont(None, 32)

# Зареждане на звук
if os.path.exists("hit.wav"):
    hit_sound = pygame.mixer.Sound("hit.wav")
else:
    hit_sound = None
    print("ВНИМАНИЕ! Звукът hit.wav не може да бъде зареден.")

clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # започваш дърпането
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
                shots_fired += 1 # Нов изстрел

        # Обработка на рестарт след удар
        elif event.type == pygame.USEREVENT:
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            target_hit = False
            pygame.time.set_timer(pygame.USEREVENT, 0)
            if not target.alive:
                target = Target(random.randint(400, 760), random.randint(0, height - 120))

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
        if bird_pos[0] > width or bird_pos[1] > height or launcher_timer > 5000:
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            target_hit = False # нова цел
    # Проверка за сблъсък с мишенага
    if target.alive:
        bird_rect = pygame.Rect(bird_pos[0] - bird_radius, bird_pos[1] - bird_radius, bird_radius * 2,
        bird_radius * 2)
        if bird_rect.colliderect(target.rect):
            target.hit()
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            hits += 1
            if hit_sound:
                hit_sound.play()
            # Рестартиране след 1 секунда
            pygame.time.set_timer(pygame.USEREVENT, 1000)

    # Рисуване
    screen.blit(bird_png, (bird_pos[0] - bird_radius, bird_pos[1] - bird_radius))
    pygame.draw.line(screen, black, (sligshot_x, sligshot_y), (int(bird_pos[0]), int(bird_pos[1])), 2)
    pygame.draw.circle(screen, black, (sligshot_x, sligshot_y), 5)

    target.draw(screen)

    # Статистика
    text1 = font.render(f'Изстрели: {shots_fired}', True, black)
    text2 = font.render(f'Удари: {hits}', True, black)
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))


    pygame.display.update()


pygame.quit()

