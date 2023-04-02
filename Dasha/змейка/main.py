import pygame
from random import randrange #
from time import sleep

pygame.init()

RES = 700 #
size = 50 #

screen = pygame.display.set_mode([RES, RES])
font = pygame.font.SysFont('Papyrus', 26, bold=True) #
# .ttf - расширение шрифта
pygame.display.set_caption('Snake')

bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def game():
    speed_count, snake_speed = 0, 10
    x, y = randrange(size, RES-size, size), randrange(size, RES-size, size)
    apple = randrange(size, RES-size, size), randrange(size, RES-size, size)
    bananas = randrange(size, RES-size, size), randrange(size, RES-size, size)
    
    dx, dy = 0, 0

    snake = [(x, y)]
    length = 1
    score = 0

    dir_t = {
        'left': True, 
        'right': True,
        'down': True,
        'up': True
    }

    fps = 60

    while True: 
        screen.blit(bg, (0, 0)) 
        #Малюємо змійку та яблуко

        [pygame.draw.rect(screen, (0, 255, 0), (i, j, size-1, size-1)) for i, j in snake]
        pygame.draw.rect(screen, (255, 0, 0), (*apple, size, size))
        pygame.draw.rect(screen, (255, 255, 0), (*bananas, size, size))
        # *apple -> x, y

        render_end = font.render("END GAME", 1, pygame.Color("orange"))
        render_score = font.render(f"SCORE {score}", 1, pygame.Color('purple'))
        # показати рахунок

        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * size
            y += dy * size
            snake.append((x, y))
            snake = snake[-length:]

        # eating food
        if snake[-1] == apple:
            apple = randrange(size, RES-size, size), randrange(size, RES-size, size)
            length += 1
            score += 1
            snake_speed -= 1
            snake_speed = max(snake_speed, 4)
        
        if snake[-1] == bananas:
            bananas = randrange(size, RES-size, size), randrange(size, RES-size, size)
            length += 1
            score -= 1
            snake_speed -= 1
            snake_speed = max(snake_speed, 4)

        #гра завершена
        if x < 0 or x > RES - size or y < 0 or y > RES - size or len(snake) != len(set(snake)):
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            sleep(3)
            game()

        exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if dir_t['up']:
                dx, dy = 0, -1
                dir_t = {
                    'left': True, 
                    'right': True,
                    'down': False,
                    'up': True
            }
        elif keys[pygame.K_s]:
            if dir_t['down']:
                dx, dy = 0, 1
                dir_t = {
                    'left': True, 
                    'right': True,
                    'down': True,
                    'up': False
            }
        elif keys[pygame.K_a]:
            if dir_t['left']:
                dx, dy = -1, 0
                dir_t = {
                    'left': True, 
                    'right': False,
                    'down': True,
                    'up': True
            }
        elif keys[pygame.K_d]:
            if dir_t['right']:
                dx, dy = 1, 0
                dir_t = {
                    'left': False, 
                    'right': True,
                    'down': True,
                    'up': True
            }
        
        # w -> up -> True
        # s -> down -> True
        # a -> left -> True
        # d -> right -> True

        screen.blit(render_score, (0, 0))
        
        clock.tick(fps)
        pygame.display.flip()
        
if __name__ == '__main__':
    game()
    sleep(5)