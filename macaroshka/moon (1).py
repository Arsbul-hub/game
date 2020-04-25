import keyboard
from random import *
import array
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
m = []
#m = Monster(10,12,l,randint(1,4))
#m1 = Monster(10,12,l,randint(1,4))
#m2 = Monster(10,12,l,randint(1,4))
#m3 = Monster(10,12,l,randint(1,4))
#m4 = Monster(10,12,l,randint(1,4))
num_m = 4
rand = random.randint(1,4)
for i in range(4):
    m.append(Monster(10,12,maps.maps(0),randint(1,4)))
while run:
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False

    x,y = h.getPos()
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
        if Lavel == 1:

                    h.move()
                    for j in m:
                        j.move()

                        mx,my = j.getPos()

                    
                        #print(h.collision_check(m[j].getPos()))
                        if h.collision_check(j.getPos()) == True:
                        
                            Plh -= 1
                            Game = False
                            Menu = True
                        
                            if Plh == 0:
                                print("fff")
                                h.setPoint()
                                #point = 0
                                Plh = 3
                                #Plh -= 1


                                #l = maps.maps(0)
                                h.l = maps.maps(0)
                                
                                break
                                
                        h.getPoint()
                                
                        

                        rect3 = surf3.get_rect(bottomright=((my+1)*23,(mx+1)*23))
                        sc.blit(surf3,rect3)
                        #
        rect2 = surf2.get_rect(bottomright=((x+1)*23,(y+1)*23))
        sc.blit(surf2,rect2)

    pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
