from pynput.mouse import Button, Controller

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
surf11 = pygame.image.load("Images/pack.png")
# ГЕРОЙ
h = Hero(10,11,l,0)
Disk = 0


class Figure(object):
    def __init__(self,x,y,mas,ftype):
       self.x=x
       self.y=y
       
       self.ftype=ftype
       self.mas=mas
       #self.mas[self.x][self.y] = 3

class player(object):

    def __init__(self, fgroup, name=None):
        self.fgroup = fgroup
        if name is None:
            self.name = "x2dred"#генератор имен(изменено)
        else:
           self.name = name
        self.list_figures = []
    def create_figure(self,x,y,xi,yi,mas,ftype=1):
         self.list_figures.append(Figure(xi,yi,mas,ftype))
    def del_fugure(self,x):
        self.mas.remove(х)
    def get_indexPos(self,mx,my,Xsize,Ysize):
        self.my = my
        self.mx = mx
        self.Xsize = Xsize
        self.Ysize = Ysize
        return int(self.mx/(self.Xsize)),int(self.my/(self.Ysize))
class Mouse(object):
    def __init__(self):

        self.flag = False
        self.flag1 = False
        self.step = 1
    def get_clik(self,but):
        
        if self.flag == False:
                self.flag = pygame.mouse.get_pressed() == but
                self.step = 1
        else:
                if pygame.mouse.get_pressed() == (0,0,0):

                          self.flag = False
                          
                          return True
        return False
        

m = Mouse()
m1 = Mouse()
m2 = Mouse()
m3 = Mouse()
p1 = player('1',1)
p2 = player('2',2)

step = 1
lmas = maps.maps(2)
fmas = maps.maps(2)
while run:
    
    # Проверка событий
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # меню hh

        

    if Menu == True and Game == False:
         for i in range(20):
            for j in range(20):
                if mas[i][j] == 1:
                    pygame.draw.rect(sc,(45,225,0),(j*32,i*32,32,32))
                if mas[i][j] == 2:
                    
                    pygame.draw.rect(sc,(200,0,0),(j*32,i*32,32,32))
         mx,my = pygame.mouse.get_pos()
         
         
         if mas[int(my/32)][int(mx/32)] == 1 and pygame.mouse.get_pressed() == (0,0,1):
             #print("g")
             Game = True
             Menu = False
         if mas[int(my/32)][int(mx/32)] == 2 and pygame.mouse.get_pressed() == (0,0,1):
            
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
        

        
        mx,my = pygame.mouse.get_pos()
        if step == 1:
            
            x1,y1 = p1.get_indexPos(mx,my,XSize/XItem,YSize/YItem)
            
            if m.get_clik((1,0,0)) == True and l[y1][x1] == 1 and lmas[y1][x1] == 0 and y1 < 3:
                #print("uu")
                
                p1.create_figure((y1)*int(XSize/XItem),(x1)*int(YSize/YItem),y1,x1,lmas,3)
                lmas[y1][x1] = 3
                #print(l[int(x1)][int(y1)])        
            elif m1.get_clik((0,1,0)) == True and len(p1.list_figures) > 1:
                step = 2

            elif m2.get_clik((0,0,1)) and len(p1.list_figures) > 1:
                p1.list_figures.pop()
                lmas[y1][x1] = 0
                print(lmas[y1][x1])
        elif step == 2:

            x1,y1 = p1.get_indexPos(mx,my,XSize/XItem,YSize/YItem)

            if m.get_clik((1,0,0)) == True and l[y1][x1] == 1 and lmas[y1][x1] == 0 and y1 > 4:
                #print("uu")
                
                p2.create_figure((y1)*int(XSize/XItem),(x1)*int(YSize/YItem),y1,x1,lmas,3)
                lmas[y1][x1] = 3
                #print(l[int(x1)][int(y1)])        
            elif m1.get_clik((0,1,0)) == True and len(p2.list_figures) > 1:
                step = 3
            elif m3.get_clik((0,0,1)) and len(p2.list_figures) > 1:
                p2.list_figures.pop()
                lmas[y1][x1] = 0
        elif step == 3:
            if m.get_clik((0,1,0)) == True:
                step = 4


        

        #print(m.get_clik())
        


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
                                        if lmas[j][i] == 3:
                                            sc.blit(pygame.transform.scale(surf11,(int(XSize/XItem),int(YSize/YItem))), ((i)*int(XSize/XItem),(j)*int(YSize/YItem)))

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





        pygame.display.update()
    #ygame.time.delay(50)               
pygame.quit()
