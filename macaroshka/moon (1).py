import keyboard
from random import *
import pygame
import maps
from Mobs import *
import time
l = maps.maps(0)
sc = pygame.display.set_mode((690,690))
run = True
Menu = True
Game = False
Lavel = 0
Plh = 3
point = 0
surf1 = pygame.image.load("Images/block.png")
surf2 = pygame.image.load("Images/pac.png")
surf3 = pygame.image.load("Images/0.png")
surf4 = pygame.image.load("Images/stars.png")
#surf5 = pygame.image.load("Images/GoodJob.png")
surf6 = pygame.image.load("Images/1.png")
#surf7 = pygame.image.load("Images/portal.png")
#surf8 = pygame.image.load("Images/stars.png")
h = Hero(10,11,l,0)
m = Monster(10,12,l,randint(1,4))
m1 = Monster(10,12,l,randint(1,4))
m2 = Monster(10,12,l,randint(1,4))
m3 = Monster(10,12,l,randint(1,4))
m4 = Monster(10,12,l,randint(1,4))
rand = random.randint(1,4)


while run:
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    for j in range(30):
        for i in range(30):
                if l[i][j] == 1:
                    pygame.draw.rect(sc,(0,0,0),((j+1)*23,(i+1)*23,23,23))
                if l[i][j] == 1:
                    rect1 = surf1.get_rect(bottomright=((j+1)*23,(i+1)*23))
                    sc.blit(surf1,rect1)
                if l[i][j] == 2:
                    rect6 = surf6.get_rect(bottomright=((j+1)*23,(i+1)*23))
                    sc.blit(surf6,rect6)
    x = h.x
    y = h.y
    point = h.point
    if Menu == True:
        rect4 = surf4.get_rect(bottomright=(690,690))
        sc.blit(surf4,rect4)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LSHIFT:
                Game = True
                Menu = False
                Lavel = 1
                sc.fill((0,0,0))
    if Game == True:
            
        if Lavel == 1:

                    h.move()
                    m.move()
                    m1.move()
                    m2.move()
                    m3.move()
                    mx = m.x
                    my = m.y
                    mx1 = m1.x
                    my1 = m1.y
                    
                    mx2 = m2.x
                    my2 = m2.y
                    
                    mx3 = m3.x
                    my3 = m3.y
                    #print(x,mx,y,my)
                    if x == my and y == mx or x == my1 and y == mx1 or x == my2 and y == mx2 or x == my3 and y == mx3:
                        Plh -= 1
                        Game = False
                        Menu = True
                    if Plh == 0:
                        time.sleep(0.5)
                        point = 0
                        Plh = 3
                    h.getPoint()
                    print(point)
                    if Game == False and Menu == True:
                        Plh -= 1
                        x = 10
                        y = 11
                        mx = 10
                        my = 10
                        mx1 = 10
                        my1 = 10   
                        mx2 = 10
                        my2 = 10
                        mx3 = 10
                        my3 = 10   
        rect2 = surf2.get_rect(bottomright=((x+1)*23,(y+1)*23))
        sc.blit(surf2,rect2)
        rect3 = surf3.get_rect(bottomright=((my+1)*23,(mx+1)*23))
        sc.blit(surf3,rect3)
        rect4 = surf3.get_rect(bottomright=((my1+1)*23,(mx1+1)*23))
        sc.blit(surf3,rect4)
        rect5 = surf3.get_rect(bottomright=((my2+1)*23,(mx2+1)*23))
        sc.blit(surf3,rect5)
        rect6 = surf3.get_rect(bottomright=((my3+1)*23,(mx3+1)*23))
        sc.blit(surf3,rect6)
    pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
