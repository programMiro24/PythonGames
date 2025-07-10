import os
import pygame
import sys
import random

MAX_PLATFORMS = 35

# инциализация
pygame.init()
pygame.mixer.init()
# екран
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Mario")
# цветове
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
# player
player_size = (35, 75)
player_x = 150
player_y = height - 150
player_vel_y = 0
on_ground = False
# платформи
platforms = [
    pygame.Rect(0, height - 50, 10000, 50),  # голяма земя
    pygame.Rect(300, height - 150, 100, 20),
    pygame.Rect(500, height - 250, 100, 20),
    pygame.Rect(700, height - 350, 100, 20)
]
# монети
coins = [
    pygame.Rect(350, height - 180, 20, 20),
    pygame.Rect(520, height - 280, 20, 20),
    pygame.Rect(720, height - 380, 20, 20),
]
scores = 0
# random platforms
platform_number = 0
is_overlap = False
min_dist_x = 75
min_dist_y = 50
last_x = 300
last_y = height - 250

while platform_number < MAX_PLATFORMS:
    platform_x = last_x + random.randint(200, 250)
    platform_y = last_y + random.randint(-90, 90)
    is_spawn_coin = random.randint(0, 100000) % 2
    platform_width = random.randint(80, 150)
    platform_y = max(100, min(platform_y, height - 150))
    platform_height = 20
    platform_rect = pygame.Rect(platform_x, platform_y,
                                platform_width, platform_height)
    is_overlap = False
    for existing in platforms:
        if platform_rect.colliderect(existing):
            is_overlap = True
            break
        # path_x = abs(platform_x - existing.x)
        # path_y = abs(platform_y - existing.y)
        # if path_x < min_dist_x and path_y < min_dist_y:
            # is_overlap = True
            # break
    if not is_overlap:
        platforms.append(platform_rect)
        platform_number += 1
        last_x = platform_x
        last_y = platform_y
        if is_spawn_coin:
            coins.append(pygame.Rect(platform_x + platform_width // 2 - 10, platform_y - 20, 20, 20))



# изображение
if os.path.exists("mario.png"):
    mario = pygame.image.load("mario.png").convert_alpha()
else:
    mario = None
    print("ВНИМАНИЕ! Не успях да заредя mario.png.")
frames=[]
for number in range(1, 13):
    if os.path.exists(f"mario{number}.png"):
        mario_pic = pygame.image.load(f"mario{number}.png").convert_alpha()
        frames.append(mario_pic)
    else:
        mario_pic = None
        print(f"ВНИМАНИЕ! Не успях да заредя mario{number}.png.")

# камера
camera_x = 0
# статистика
font = pygame.font.SysFont(None, 30)
# animation
# frame2 = pygame.image.load("mario2.png").convert_alpha()

#if mario or mario2:
    #frames = [mario, mario2]
#else:
    #frames = None

# animation settings
current_frame = 0
frame_duration = 200  # време между кадри в милисекунди
last_update = pygame.time.get_ticks()

is_animated = False
is_left = False
is_stopped = False

# main loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -5
        is_left = True
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 5
        is_left = False
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = -15
        on_ground = False
    is_animated = keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]

    player_x += dx

    # гравитация
    player_vel_y += 1 # тежест
    player_y += player_vel_y

    # проверка за край
    if player_y > height:
        screen.fill(black)
        font = pygame.font.SysFont(None, 60)
        text = font.render("Ти загуби!", True, red)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 30))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # проверка за платформи
    on_ground = False
    player_rect = pygame.Rect(player_x, player_y, *player_size)
    for platform in platforms:
        if platform.colliderect(player_rect) and player_vel_y >= 0:
            player_y = platform.top - player_size[1]
            player_vel_y = 0
            on_ground = True
    # монети
    for coin in coins:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            scores += 1

    # Камера
    camera_x = player_x - width // 2

    screen.fill(white)
    # рисуване на платформи
    for platform in platforms:
        platform_screen = platform.move(-camera_x, 0)
        pygame.draw.rect(screen, green, platform_screen)

    # рисуване на играча
    now = pygame.time.get_ticks()

    # Смяна на кадър
    if is_animated and frames:
        if current_frame == len(frames) - 1:
            frame_duration = 150  # 1 секунда пауза на последния кадър
        else:
            frame_duration = 50  # нормална пауза
        if now - last_update >= frame_duration and is_animated:
            current_frame = (current_frame + 1) % len(frames)
            last_update = now
    else:
        is_stopped = True
    if frames:
        frame_image = frames[current_frame]
        if is_stopped:
            frame_image = mario
        if is_left:
            frame_image = pygame.transform.flip(frame_image, True, False)
        screen.blit(frame_image, (player_x - camera_x, player_y))
    else:
        player_screen_rect = pygame.Rect(player_x - camera_x, player_y, *player_size)
        pygame.draw.rect(screen, blue, player_screen_rect)

    # рисуване на монети
    for coin in coins:
        coin_screen = coin.move(-camera_x, 0)
        pygame.draw.circle(screen, (255, 223, 0), coin_screen.center, 10)  # златиста монета
    text = font.render(f"Точки: {scores}", True, black)
    screen.blit(text, (10, 10))
    is_stopped = False

    pygame.display.flip()



pygame.quit()
sys.exit()
