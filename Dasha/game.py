import pygame

pygame.init()

w, h = 600, 600
x, y = 0, 0
size = (w, h)
color = (255, 255, 255)

sc = pygame.display.set_mode(size)

run = True 
while run:
    img = pygame.image.load("bbb.webp").convert_alpha() # фон
    sc.blit(img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y > 0:
                    y -= 90
            if event.key == pygame.K_DOWN:
                if y < h-30:
                    y += 30
            if event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 30
            if event.key == pygame.K_RIGHT:
                if x < w-30:
                    x += 30
        if y < h-30:
            y += 30
        
        if y >= 450 and y >= 480+30 and x >= 170 and x <= 230:
            y -= 30 

    sq = pygame.Rect(x, y, 30, 30)
    pygame.draw.rect(sc, (0, 0, 0), sq)

    tt1 = pygame.Rect(450, 200, 120, 30)
    pygame.draw.rect(sc, (100, 100, 100), tt1)

    tt2 = pygame.Rect(200, 450, 120, 30)
    pygame.draw.rect(sc, (200, 200, 200), tt2)

    txt = pygame.font.SysFont("Ariel", 66, bold = True)
    r_txt = txt.render("Welcome", 1, (255, 0, 0))
    sc.blit(r_txt, (w / 3, h / 3)) 
      
    pygame.display.flip() # рендеринг