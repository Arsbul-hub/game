import maps1
import pygame
import keyboard
sc = pygame.display.set_mode((1050,300))
surf6 = pygame.image.load("Images/block.png")
l = maps1.ret()
run = True
minx = 0
maxx = 10
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    for i in range(minx,maxx):
        for j in range(30):
            #if l[i][j] == 1:
                    rect5 = surf6.get_rect(bottomright=(j*20,i*20))
                    sc.blit(surf6,rect5)
                    if keyboard.is_pressed('r') == True:
                        minx+=1
                        maxx+=1
    print(minx,maxx)                    
    pygame.display.update()
pygame.quit()
