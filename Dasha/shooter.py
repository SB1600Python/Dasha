import pygame
from copy import deepcopy
from bullet import Bullet
from player import Player, Enemy


pygame.init()

x, y = 0, 0
w, h = 600, 600

l, r = False, False

#Игрок
player_left = pygame.image.load("left/left.png")
player_right = pygame.image.load("right/right.png")
player_stand = pygame.image.load("stand/stand.png")

sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Game")

bg = pygame.image.load("bg.jpg") #Фон

shoot = False

bullet_x = 0
bullet_y = 0

enemy_x = 0
enemy_y = 0

enemy_left = False
enemy_right = False

enemy = False

health = 3

direction = []

player = Player(x, y, player_left)

run = True
while run:

    sc.blit(bg, (0, 0)) #Фон

    for event in pygame.event.get():
        #Выход 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: #Прыжок
            if y >= h-90:
                if event.key == pygame.K_UP:
                    y -= h/20
                if event.key == pygame.K_SPACE:
                    bullet_x, bullet_y = (deepcopy(x) + 30), (deepcopy(y) + 30)
                    shoot = True
            if event.key == pygame.K_1:
                enemy = True
                enemy_x = w-30
                enemy_y = h-50
    
    if y < h-50: 
        y += 1
    elif x < -30:
        x += w+30
    elif x > w-30:
        x -= w+30
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
        l, r = True, False
    if keys[pygame.K_RIGHT]:
        x += 1
        l, r = False, True

    if l:
        sc.blit(player_left, (x, y))
    elif r:
        sc.blit(player_right, (x, y))
    else:
        sc.blit(player_stand, (x, y))


    if x in range(w-150, w-30):
        if y in range(h-80, h-60):
            y -= 1
        elif y in range(h-60, h+30):
            if l:
                x += 1
            if r:
                x -= 1
    

    pygame.draw.rect(sc, (55, 55, 0), (w-120, h-30, 90, 30))


    if shoot:
        if l or r:
            direction.append((l, r))
        else:
            shoot = False
            direction.clear()

        if bullet_x <= 0 or bullet_x >= w:
            shoot = False
            direction.clear()
        
        if direction:
            if direction[0][0]:
                bullet_x -= 2
                bullet_y += 0.1
            elif direction[0][1]:
                bullet_x += 2

        bullet1 = Bullet(bullet_x, bullet_y, 'bullet.png') #Мяч
        sc.blit(bullet1.image, bullet1.rect)

    if enemy:
        if enemy_x >= -30 and enemy_x >= x:
            enemy_left = True
            enemy_right = False
        elif enemy_x <= w-30:
            enemy_left = False
            enemy_right = True
        else:
            enemy = False

        if enemy_left:
            enemy_x -= w + 30
        if enemy_x == x:
            if health <= 0:
                run = False
            else:
                health -= 1

    print(health)

    sc.blit(player_left, (enemy_x, enemy_y))

    pygame.display.flip() #Рендеринг
