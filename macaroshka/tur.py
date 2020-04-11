import maps1
import pygame
import keyboard
sc = pygame.display.set_mode((1050,300))
l = maps1.ret()
run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    for i in range(10):
        for j in range(35):
            if l[j][i] == 1:
                
pygame.quit()
