import maps
l =    maps.maps(0)    
import random
import pygame
import os
pygame.init()
sc = pygame.display.set_mode((690,690))
run = True
menu = 0
game = 0
lav = 1
#print(ins)
##########
#мпорт картинок
surf6 = pygame.image.load("Images/block.png")
surf7 = pygame.image.load("Images/pac.png")
surf8 = pygame.image.load("Images/0.png")
surf9 = pygame.image.load("Images/GoodJob.png")
surf10 = pygame.image.load("Images/stars.png")
surf11 = pygame.image.load("Images/1.png")
surf12 = pygame.image.load("Images/portal.png")
surf13 = pygame.image.load("Images/stars.png")
##########

x = 10
y = 10
#######
mx = 3
my = 20
#######
mx1 = 3
my1 = 10
#######
mx2 = 10
my2 = 15
#######
mx3 = 12
my3 = 10
#######
mx4 = 25
my4 = 10
#######
import gost
import keyboard
##########
lavel = 0# коло-во точек
##########
rand = random.randint(1,4)
rand1 = random.randint(1,4)
rand2 = random.randint(1,4)
rand3 = random.randint(1,4)
rand4 = random.randint(1,4)

tick = 0# относится к таймеру
pin = 0#кол-во монстров в клетке
bh = 100#здоровье босса
good = 5#таймер2
gtick = 0#относится к таймеру
timer = 400#таймер
#gameover = 0# 
h = 3# здоровье
g1 = ''# пауза
import array

pygame.display.set_caption("PacStars | alpha 0.2")
#призраки
m1 = gost.monsters(l,mx,my,rand)
m2 = gost.monsters(l,mx1,my1,rand1)
m3 = gost.monsters(l,mx2,my2,rand2)
m4 = gost.monsters(l,mx3,my3,rand3)
m5 = gost.monsters(l,mx4,my4,rand4)
##
s = 50
e = []

while run:
    pygame.time.delay(50)
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                g1 = "pause"
        if ev.type == pygame.QUIT:
            run = False
            
##таймер времяни
    tick+=0.1
    if lav != 4:
        if tick > 0.9 and game == 1:
            tick = 0
            timer-=1
        if menu == 0 and h == 0:
            
            timer = 400
#######
#########отрисовка текстур по массиву
        f12 = pygame.font.SysFont(None, 36)
    
    for j in range(30):
            for i in range(30):
                if game == 1 and menu == 1:
                    if l[j][i] == 0:
                        pygame.draw.rect(sc,(0,0,0),((i+1)*23,(j+1)*23,20,20))
                    if l[j][i] == 1:
                        rect5 = surf6.get_rect(bottomright=((i+1)*23,(j+1)*23))
                        sc.blit(surf6,rect5)
                    if l[j][i] == 2:
                        rect10 = surf11.get_rect(bottomright=((i+1)*23,(j+1)*23))
                        sc.blit(surf11,rect10)
                    if l[j][i] == 3:
                        rect11 = surf12.get_rect(bottomright=((i+1)*23,(j+1)*23))
                        sc.blit(surf12,rect11)
#######
#######пауза
    if g1 == "pause":
        menu = 1
######меню
    if menu == 0 and game == 0:



        if h == 0:
            h = 3
            lavel = 0
            timer = 400
            x = 10
            y = 10
           
            l = maps.maps(0)
        if h > 0 and g1 != "pause":


            mx = 3
            my = 20
            #######
            mx1 = 3
            my1 = 10
            #######
            mx2 = 10
            my2 = 15
            #######
            mx3 = 12
            my3 = 10
            #######
            mx4 = 25
            my4 = 10
#####пауза

        if g1 == "pause":
            if ev.type == pygame.KEYDOWN:
                if keyboard.is_pressed('escape')== True:
                    g1 = ""
######текст                    
        rect16 = surf13.get_rect(bottomright=(690,690))
        sc.blit(surf13,rect16)
        f12 = pygame.font.SysFont(None, 36)

        text12 = f12.render("Управление: W,S,A,D.", 1, (255, 45, 0))
        sc.blit(text12,(0,420))
        f12 = pygame.font.SysFont(None, 36)

        text12 = f12.render("Отлов прешельцев: SPASE,", 1, (255, 45, 0))
        sc.blit(text12,(0,440))
        f12 = pygame.font.SysFont(None, 36)
        
        text12 = f12.render("только при контакте с ними.", 1, (255, 45, 0))
        sc.blit(text12,(0,460))
        f12 = pygame.font.SysFont(None, 36)
        
        text12 = f12.render("Shift - Старт", 1, (255, 45, 0))
        sc.blit(text12,(0,480))
######сплеши
        if s == 40:
            e = 1
        elif s == 50:
            e = 0
        if e == 0:
            s -= 2
        elif e == 1:
            s += 2
            
        gost.monsters.setText(sc,250,150,s,(45,255,0),"Сейчас в 2d")
######инструкция
    gost.monsters.setText(sc,0,0,36,(180, 0, 0),"Время:" + str(timer) + ';')


    gost.monsters.setText(sc,120,0,36,(180, 0, 0),"   Очки: "+str(lavel))

    if lavel != 3:###если не бой с боссом
        gost.monsters.setText(sc,300,0,36,(180, 0, 0),"Здоровье: "+str(h))
########старт
    if timer == 0:
        menu = 0
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_LSHIFT and menu == 0:
            menu = 0
            game = 1
            if game > 1:
                game-=1
            sc.fill((0,0,0))

            lavel = 0
########игра
    if game == 1: # монстры
############################################################
                if l[y][x] == 2:
                    lavel += 1
                    l[y][x] = 0

                m1.move()
                mx,my = m1.getPos()
############################################################

                m2.move()
                mx1,my1 = m2.getPos()
############################################################


                m3.move()
                mx2,my2 = m3.getPos()
############################################################

                m4.move()
                mx3,my3 = m4.getPos()
############################################################               

                if lavel < 422:##если попались монстрам без точек

                    if  mx == x and my == y or x == mx and y == my or mx1 == x and my1 == y or x == mx1 and y == my1 or mx2 == x and my2 == y or x == mx2 and y == my2 or mx3 == x and my3 == y or x == mx3 and y == my3:

                        h -= 1
                        menu = 0
                if lavel > 422:#если собрали точка ловим пришельцев
                    
                    if keyboard.is_pressed(' ') == True:
                            if mx == x and my == y or x == mx and y == my:
                                pin += 1
                                my = 3
                                mx = 3
                            if mx1 == x and my1 == y or x == mx1 and y == my1:
                                pin += 1
                                my1 = 3
                                mx1 = 3
                            if mx2 == x and my2 == y or x == mx2 and y == my2:
                                pin += 1
                                my2 = 3
                                mx2 = 3
                            if mx3 == x and my3 == y or x == mx3 and y == my3:
                                pin += 1
                                my3 = 3
                                
                                mx3 = 3
                    if  pin == 4:#если пришельцы в камере
                        l = maps.maps(1)
                    
                if l[y][x] == 3:#если вошли в портал
                        x =  25
                        y = 10
                        lav = 3
    if lav == 3:#бой с боссом

                
                if keyboard.is_pressed(' ') == True and x == mx4 and y == my4:# бьём босса

                    bh -= 2
                m5.move()
                mx4,my4 = m5.getPos()                
                f1 = pygame.font.SysFont(None, 36)

                text1 = f1.render("boss health: "+str(bh)+"%", 1, (180, 0, 0))
                sc.blit(text1,(300,0))

                l = maps.maps(2)
                if bh == 0:
                    lav = 4
    if lav == 4:# таймер заставки
        gtick+=0.1
                    
        if gtick > 1.5 and game == 1:
            gtick = 0
            good-=1
        if good != 0:
            mx4 = 3
            my4 = 28
                        
        rect8 = surf9.get_rect(bottomright=(690,690))
        sc.blit(surf9,rect8)

        if good == 0:
            
            menu = 0
            good = 5
        
                   
        

    if game ==  1 and lav != 4:#управление
        if lav != 4:
            if keyboard.is_pressed('r') == True:
                lav = 3
#                bh = 0
            if keyboard.is_pressed('w') and l[y-1][x] != 1:
                
                y -= 1
            if keyboard.is_pressed('s') and l[y+1][x] != 1:
                y += 1
            if keyboard.is_pressed('d') and l[y][x+1] != 1:
                x += 1
            if keyboard.is_pressed('a') and l[y][x-1] != 1:
                x -= 1
        gost.monsters.setImg(sc,(x+1)*23,(y+1)*23,"Images/pac.png")
        gost.monsters.setImg(sc,(mx+1)*23,(my+1)*23,"Images/0.png")
        gost.monsters.setImg(sc,(mx1+1)*23,(my1+1)*23,"Images/0.png")
        gost.monsters.setImg(sc,(mx2+1)*23,(my2+1)*23,"Images/0.png")
        gost.monsters.setImg(sc,(mx3+1)*23,(my3+1)*23,"Images/0.png")
        if lav == 3:#босс
            rect16 = surf8.get_rect(bottomright=((mx4+1)*23,(my4+1)*23))
            sc.blit(surf8,rect16)
    pygame.display.update()
#    pygame.time.delay(50)               
pygame.quit()
