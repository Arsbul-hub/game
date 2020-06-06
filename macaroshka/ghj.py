import pygame
import keyboard
sc = pygame.display.set_mode((690,690))
run = True
while run:
    # Проверка событий
    sc.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    for i in range(10):
        for j in range(10):
            if keyboard.is_pressed('d') == True:
                i+=1
                
pygame.quit()
