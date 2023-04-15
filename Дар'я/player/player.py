import pygame
import os
import sys


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Music Player')

music = os.listdir('music')

music_path = os.path.join('music', mus) #'назва папки', 'назва файлу'
pygame.mixer.music.load(music_path)
print(mus)
    
music = musicList(music)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
        self.original_width = width
        self.original_height = height

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)
    
    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = pygame.Color('black')
            self.rect.width = self.original_width - 10
            self.rect.height = self.original_height - 10
        else:
            self.color = pygame.Color('orange')
            self.rect.width = self.original_width
            self.rect.height = self.original_height
    
    def run_action(self):
        self.action()
    
    def next(self):
        global music
        music = musicList(music)
        return music

def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

play_button = Button(50, 100, 100, 50, 'Play', (0, 250, 0), play_music)
pause_button = Button(250, 100, 100, 50, 'Pause', (255, 250, 0), pause_music)
stop_button = Button(350, 100, 100, 50, 'Stop', (255, 0, 0), stop_music)
next_button = Button(270, 300, 100, 50, 'Next', (255, 0, 0), next)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            play_button.check_hover(mouse_pos)
            pause_button.check_hover(mouse_pos)
            stop_button.check_hover(mouse_pos)
            next_button.check_hover(mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if play_button.rect.collidepoint(mouse_pos):
                play_button.run_action()
            elif pause_button.rect.collidepoint(mouse_pos):
                pause_button.run_action()
            elif stop_button.rect.collidepoint(mouse_pos):
                stop_button.run_action()
            elif next_button.rect.collidepoint(mouse_pos):
                next_button.run_action()

    screen.fill((255, 255, 255))
    play_button.draw()
    pause_button.draw()
    stop_button.draw()
    next_button.draw()
    pygame.display.update()

pygame.quit()
sys.exit()
