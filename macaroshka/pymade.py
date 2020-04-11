import pygame
class set():
    def __init__(self,img,obj,x,y,scr,color,text):
        self.img = img
        self.obj = obj
        self.x = x
        self.y = y
        self.scr = scr
        self.color = color
        self.text = text

#        self.img = img
    def Img(self):
        surf = pygame.image.load(self.img)
        rect = surf.get_rect(bottomright=(self.x,self.y))
        self.obj.blit(surf,rect)
    def Text(self):
        f = pygame.font.SysFont(None, scr)
        tex = f.render(self.text, 1, self.color)
        obj.blit(tex,(self.x,self.y))
