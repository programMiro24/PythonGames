import pygame

# инциализация на pygame
pygame.init()
# размер на прозореца
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invaders")
color_screen=(7, 3, 26)
color_player=(255,0,0)
#играч
player_width=50
player_hight=30
player_x=width//2-player_width//2
player_y=height-player_hight-10
player_speed=5



clock=pygame.time.Clock()
running = True
while running:
    clock.tick(60)      #60 FPS 
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    #проверка на клавиатурата
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x>0 :
        player_x=player_x-player_y
    if keys[pygame.K_RIGHT] and player_x<width-player_width:
        player_x=player_x+player_speed

    screen.fill(color_screen)
    pygame.draw.rect(screen,color_player,(player_x,player_y,player_width, player_hight))
    pygame.display.flip()
pygame.quit()
