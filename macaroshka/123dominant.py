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
        x = h.x 
        y = h.y 
        x,y = h.getPos() 

        for j in range(8):
                                for i in range(8):


                                        if l[j][i] == 1:

                                           #pygame.draw.rect(sc,(0,0,0),((j+1)*23,(i+1)*23,23,23))
                                            rect1 = surf1.get_rect(bottomright=((i+1)*80,(j+1)*80))
                                            sc.blit(surf1,rect1)
                                        #if l[j][i] == 0:
                                        #   pygame.draw.rect(sc,(0,0,0),((i+1)*23,(j+1)*23,23,23))
                                        if l[j][i] == 0:
                                            rect10 = surf10.get_rect(bottomright=((i+1)*80,(j+1)*80))
                                            sc.blit(surf10,rect10)
                                            

        pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
