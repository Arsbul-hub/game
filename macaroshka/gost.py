import random
import pygame
class monsters(object):
    def __init__(self,l,m1,m2,rand):
        self.l = l
        self.mx = m1
        self.my = m2
        self.rand = rand
#        self.img = img
    def move(self):


        if self.rand == 1:
            self.my += 1
            if self.l[self.my][self.mx] == 1:
                self.my-=1
                self.rand = random.randint(1,4)
        if self.rand == 2:
            self.my -= 1
            if self.l[self.my][self.mx] == 1:
                self.my+=1
                self.rand = random.randint(1,4)
        if self.rand == 3:
            self.mx +=1
            if self.l[self.my][self.mx] == 1:
                self.mx-=1
                self.rand = random.randint(1,4)
        if self.rand == 4:
            self.mx -= 1
            if self.l[self.my][self.mx] == 1:
                self.mx+=1
                self.rand = random.randint(1,4)
    def setImg(obj,x,y,img):
        surf = pygame.image.load(img)
        rect = surf.get_rect(bottomright=(x,y))
        obj.blit(surf,rect)
    def setText(obj,x,y,scr,color,text):
        f = pygame.font.SysFont(None, scr)
        text = f.render(text, 1, color)
        obj.blit(text,(x,y))
    def getPos(self):
        return self.mx,self.my
