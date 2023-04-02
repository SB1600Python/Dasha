import pygame

#Направление 
left = False
right = False

#Персонаж
left_p = pygame.image.load(f'left/left.png')
right_p = pygame.image.load(f'right/right.png')
stand_p = pygame.image.load(f'stand/stand.png')

#Определение констант

#РАЗМЕР ЕКРАНА
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#РАЗМЕР ИГРОКА
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
#ПРЫЖОК
JUMP_HEIGHT = 100
#НАПРАВЛЕНИЕ КАМЕРЫ
CAMERA_WIDTH = (SCREEN_WIDTH // 2) - PLAYER_WIDTH
CAMERA_HEIGHT = (SCREEN_HEIGHT // 2) - PLAYER_HEIGHT

BACKGROUND_IMAGE = "bg.jpg"

#Инициализация Pygame
pygame.init()

#Создание екрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Создание фона
background = pygame.image.load(BACKGROUND_IMAGE).convert()

#Создание игрока x: 0, y: 0, width: PLAYER_WIDTH
# player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)



#Определение начальной позиции игрока
x = (SCREEN_WIDTH // 2) - PLAYER_WIDTH
y = SCREEN_HEIGHT - PLAYER_HEIGHT

#Создание камеры
camera = pygame.Rect(0, 0, CAMERA_WIDTH, CAMERA_HEIGHT)

#оПРЕДЕЛЕНИЕ ФУНКЦИИ ДЛЯ ПЕРЕДВИЖЕНИЯ ИГРОКА
def move_player(dx, dy):
    global x, y

    x += dx
    y += dy

    #Проверка на выход за границы экрана
    if x < 50:
        x += 1
    elif x > SCREEN_WIDTH - PLAYER_WIDTH:
        x = SCREEN_WIDTH - PLAYER_WIDTH
    
    if y < 0:
        y = 0
    elif y > SCREEN_HEIGHT - PLAYER_HEIGHT:
        y = SCREEN_HEIGHT - PLAYER_HEIGHT

    return x, y

#Определение функции для прыжка
def jump():
    global y
    start_y = y
    for i in range(JUMP_HEIGHT):
        y -= 1
        if y < 0:
            y = 0
        screen.blit(background, (-camera.x, -camera.y))
        print(x, y)
        screen.blit(stand_p, (x, y))
        pygame.display.flip()
    for i in range(JUMP_HEIGHT):
        y += 1
        if y > SCREEN_HEIGHT - PLAYER_HEIGHT:
            y = SCREEN_HEIGHT - PLAYER_HEIGHT
        screen.blit(background, (-camera.x, -camera.y))
        screen.blit(stand_p, (x, y))
        pygame.display.flip()

#Основной игровой цикл
running = True
while running:
    #Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x, y = move_player(-1, 0)
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        x, y = move_player(1, 0)
        left = False
        right = True

    #Обновление камеры
    camera.x = x - CAMERA_WIDTH // 2
    camera.y = y - CAMERA_HEIGHT // 2

    #Отрисовка фона и игрока
    screen.blit(background, (-camera.x, -camera.y))
    screen.blit(stand_p, (x, y))

    pygame.display.flip()