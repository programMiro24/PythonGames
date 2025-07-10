import pygame
import math
import random

# Инциализация на pygame
pygame.init()
pygame.mixer.init()

# Прозореца
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Angry Birds")

# Цветове
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
black = (0, 0, 0)

# Позиция на прашкатаа
sligshot_x, sligshot_y = 150, height - 200

# Състояние
dragging = False
bird_pos = [sligshot_x, sligshot_y]
bird_velocity = [0, 0]
bird_radius = 15
gravity = 0.5
launced = False
launcher_timer = 0

# Мишена
target_rect = pygame.Rect(800, height - 120, 40, 40)
target_hit = False

new_game = False

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
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = sligshot_x - mouse_x
                dy = sligshot_y - mouse_y
                bird_velocity = [dx * 0.2, dy * 0.2]

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
        if (bird_pos[0] > width or bird_pos[1] > height or launcher_timer > 5000):  # and not target_hit:
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
    # Проверка за сблъсък с мишенага
    if not target_hit:
        bird_rect = pygame.Rect(bird_pos[0] - bird_radius, bird_pos[1] - bird_radius, bird_radius * 2,
        bird_radius * 2)
        if bird_rect.colliderect(target_rect):
            target_hit = True
            bird_pos = [sligshot_x, sligshot_y]
            bird_velocity = [0, 0]
            launced = False
            new_game = True

    # Рисуване
    pygame.draw.circle(screen, red, (int(bird_pos[0]), int(bird_pos[1])), bird_radius)
    pygame.draw.line(screen, black, (sligshot_x, sligshot_y), (int(bird_pos[0]), int(bird_pos[1])), 2)
    pygame.draw.circle(screen, black, (sligshot_x, sligshot_y), 5)
    if not target_hit:
        pygame.draw.rect(screen, green, target_rect)
    if new_game:
        target_rect = pygame.Rect(random.randint(400, 800 - 60), random.randint(0, height - 120), 40, 40)
        target_hit = False
        launced = dragging = False
        new_game = False



    pygame.display.update()


pygame.quit()

