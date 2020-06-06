import keyboard
from random import *
import array
import pygame
import maps
import math
from Mobs import *
import time
l = maps.maps(0)
sc = pygame.display.set_mode((640,640))
run = True

Game = True
Lavel = 0
surf1 = pygame.image.load("Images/block.png")
surf2 = pygame.image.load("Images/pac.png")
surf3 = pygame.image.load("Images/0.png")
surf4 = pygame.image.load("Images/stars.png")
surf5 = pygame.image.load("Images/ioi.png")
surf6 = pygame.image.load("Images/1.png")
surf7 = pygame.image.load("Images/portal.png")
#surf8 = pygame.image.load("Images/stars.png")
surf9 = pygame.image.load("Images/GoodJob.png")
surf10 = pygame.image.load("Images/wh.png")
# ГЕРОЙ
h = Hero(10,11,l,0)
# монстры

wx  = 640
lx = 80
mx = wx/2

#VEW_Fragment_xy = 
wy  = 640
ly = 80
my = wy/2
while run:
    # Проверка событий
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # меню

 
    # игра
    
    if Game == True:
        h.move() 
        mi = h.x 
        mj = h.y 
        x,y = h.getPos() 
        print(x,y) 
        limy = int(math.ceil((wy-ly)/2/ly))
        limx = int(math.ceil((wx-lx)/2/lx))

        #ygame.display.update()
        for j in range(mj-limy,mj+limy+2):
                                for i in range(mi-limx,mi+limx+2):


                                        if l[j][i] == 1:

                                           #pygame.draw.rect(sc,(0,0,0),((j+1)*23,(i+1)*23,23,23))
                                            rect1 = surf1.get_rect(bottomright=(math.ceil(mx + (i - mi) * lx - lx/2),math.ceil(my + (j - mj) * ly - ly/2)))
                                            sc.blit(surf1,rect1)
                                        #if l[j][i] == 0:
                                        #   pygame.draw.rect(sc,(0,0,0),((i+1)*23,(j+1)*23,23,23))
                                        if l[j][i] == 0:
                                            rect10 = surf10.get_rect(bottomright=(math.ceil(mx + (i - mi) * lx - lx/2),math.ceil(my + (j - mj) * ly - ly/2)))
                                            sc.blit(surf10,rect10)
                                            
        rect2 = surf2.get_rect(bottomright=(math.ceil(mx + (mi - mi) * lx - lx/2),math.ceil(my + (mj - mj) * ly - ly/2)))
        sc.blit(surf2,rect2)
        pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
