import keyboard
import random
import pygame
import maps
l = maps.maps(0)
sc = pygame.display.set_mode((690,690))
run = True
Menu = True
Game = False
Lavels = 0
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
x = 10
y = 10
mx = 10
my = 10
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
    
    if Menu == True:
        rect4 = surf4.get_rect(bottomright=(690,690))
        sc.blit(surf4,rect4)
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LSHIFT:
                Game = True
                Menu = False
                Lavels = 1
                sc.fill((0,0,0))
    if Game == True:
            
        if Lavels == 1:
                    if rand == 1:
                        mx += 1
                        if l[mx][my] == 1:
                            mx-=1
                            rand = random.randint(1,4)
                    if rand == 2:
                            mx -= 1
                            if l[mx][my] == 1:
                                mx+=1
                                rand = random.randint(1,4)
                    if rand == 3:
                            my +=1
                            if l[mx][my] == 1:
                                my-=1
                                rand = random.randint(1,4)
                    if rand == 4:
                            my -= 1
                            if l[mx][my] == 1:
                                my+=1
                                rand = random.randint(1,4)
                    if x == mx and y == my:
                        print("gameover")
                        Game = False
                        Menu = True
                        Plh -= 1
                        mx = 10
                        my = 10
                        x = 10
                        y = 10
                    if l[y][x] == 2:
                        point += 1
                        l[y][x] = 0
                    if keyboard.is_pressed('w') and l[y-1][x] != 1:
                        
                        y -= 1
                    if keyboard.is_pressed('s') and l[y+1][x] != 1:
                        y += 1
                    if keyboard.is_pressed('d') and l[y][x+1] != 1:
                        x += 1
                    if keyboard.is_pressed('a') and l[y][x-1] != 1:
                        x -= 1

        rect2 = surf2.get_rect(bottomright=((x+1)*23,(y+1)*23))
        sc.blit(surf2,rect2)
        rect3 = surf3.get_rect(bottomright=((my+1)*23,(mx+1)*23))
        sc.blit(surf3,rect3)
    pygame.display.update()
    pygame.time.delay(50)               
pygame.quit()
