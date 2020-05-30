import keyboard
from random import *
import array
import pygame
import maps
import math
from Mobs import *
import time
l = maps.maps(0)
sc = pygame.display.set_mode((140,140))
run = True
Menu = True
Game = False
Lavel = 0


















#мпорт моделей
surf1 = pygame.image.load("Images/block.png")
surf2 = pygame.image.load("Images/pac.png")
surf3 = pygame.image.load("Images/0.png")
surf4 = pygame.image.load("Images/stars.png")
surf5 = pygame.image.load("Images/ioi.png")
surf6 = pygame.image.load("Images/1.png")
surf7 = pygame.image.load("Images/portal.png")
#surf8 = pygame.image.load("Images/stars.png")
surf9 = pygame.image.load("Images/GoodJob.png")

# ГЕРОЙ
h = Hero(10,11,l,0)
# монстры
mi = h.mi
wx  = 140
lx = 30
mx = wx/2

mj = h.mj
wy  = 140
ly = 30
my = wy/2
while run:
    # Проверка событий
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # меню

    if Menu == True:
        rect4 = surf4.get_rect(bottomright=(690,690))
        sc.blit(surf4,rect4)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LSHIFT:
                Game = True
                Menu = False
                Lavel = 1
                sc.fill((0,0,0))
    # игра
    
    if Game == True:
        h.move()
        x,y = h.getPos()
        limy = int(math.ceil((wy-ly)/2/ly))
        limx = int(math.ceil((wx-lx)/2/lx))
        rect2 = surf2.get_rect(bottomright=((x+1)*23,(y+1)*23))
        sc.blit(surf2,rect2)
        
        



                    
                        
                            





                                    



                             

        for j in range(mi-limy,mi+limy+1):
                                for i in range(mj-limx,mj+limx+1):



                                        if l[j][i] == 1:

                                           #pygame.draw.rect(sc,(0,0,0),((j+1)*23,(i+1)*23,23,23))
                                            rect1 = surf1.get_rect(bottomright=(math.ceil(my + (j - mj) * ly - ly/2),math.ceil(mx + (i - mi) * lx - lx/2)))
                                            sc.blit(surf1,rect1)
                                        #if l[j][i] == 0:
                                        #   pygame.draw.rect(sc,(0,0,0),((i+1)*23,(j+1)*23,23,23))
        # lavel
#d
    pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
