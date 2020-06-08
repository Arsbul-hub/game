import keyboard
from random import *
import array
import pygame
import maps
import math
from Mobs import *
import time
Display = pygame.display
Size = (640,640)
Items = (8,8)
Buttons = (20,20)
l = maps.maps(0)
mas = maps.maps(1)
sc = Display.set_mode(Size)
run = True

Game = False
Menu = True
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
Disk = 0
while run:
    # Проверка событий
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # меню
    if Menu == True and Game == False:
         for i in range(20):
            for j in range(20):
                if mas[i][j] == 1:
                    pygame.draw.rect(sc,(45,225,0),(j*32,i*32,32,32))
                if mas[i][j] == 2:
                    
                    pygame.draw.rect(sc,(200,0,0),(j*32,i*32,32,32))
         mx,my = pygame.mouse.get_pos()
         
         
         if mas[int(my/32)][int(mx/32)] == 1 and pygame.mouse.get_pressed() == (1,0,0):
             #print("g")
             Game = True
             Menu = False
         if mas[int(my/32)][int(mx/32)] == 2 and pygame.mouse.get_pressed() == (1,0,0):
            
            if Disk == 0:
                 Size = (160,160)
                 Disk = 1
                 
            elif Disk == 1:
                Size = (560,560)
                Disk = 2
                
            elif Disk == 2:
                Size = (856,456)
                Disk = 3
                
            elif Disk == 3:
                Size = (640,640)
                Disk = 0
            Display.set_mode(Size)
         pygame.display.update()
    # игра
    
    if Game == True and Menu == False:
        XSize,YSize = Size
        XItem,YItem = Items
        h.move() 
        x = h.x 
        y = h.y 
        x,y = h.getPos() 

            #
            
        for j in range(8):
                                for i in range(8):


                                        if l[j][i] == 1:

                                            #pygame.draw.rect(sc,(0,0,0),(j*23,i*23,23,23))
                                            sc.blit(pygame.transform.scale(surf1,(int(XSize/XItem),int(YSize/YItem))), ((i)*int(XSize/XItem),(j)*int(YSize/YItem)))
                                        #if l[j][i] == 0:
                                        #   pygame.draw.rect(sc,(0,0,0),((i+1)*23,(j+1)*23,23,23))
                                        if l[j][i] == 0:
                                            
                                             


                                            
                                            sc.blit(pygame.transform.scale(surf10,(int(XSize/XItem),int(YSize/YItem))), ((i)*int(XSize/XItem),(j)*int(YSize/YItem)))
                                            #print(pygame.transform.get_smoothscale_backend())
                                            #sc.blit(surf10,rect10)
        ButtonX,ButtonY = Buttons
        for i in range(20):
            for j in range(20):
                if mas[i][j] == 2:
                    
                    pygame.draw.rect(sc,(200,0,0),(j*int(XSize/ButtonX),i*int(YSize/ButtonY),int(XSize/ButtonX),int(YSize/ButtonY)))
        mx,my = pygame.mouse.get_pos()
         
         

        if mas[int(my/int(YSize/ButtonY))][int(mx/int(XSize/ButtonX))] == 2 and pygame.mouse.get_pressed() == (1,0,0):
            
            if Disk == 0:
                 Size = (160,160)
                 Disk = 1
                 
            elif Disk == 1:
                Size = (560,560)
                Disk = 2
                
            elif Disk == 2:
                Size = (856,456)
                Disk = 3
                
            elif Disk == 3:
                Size = (640,640)
                Disk = 0
            Display.set_mode(Size)                                            
                                        #print(math.ceil(5.55,1))
        pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
