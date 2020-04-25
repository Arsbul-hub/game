import keyboard
import random
class Mob(object):
    def __init__(self,mx,my):
        self.x = mx
        self.y = my
    def move():
        raise NotImplementedError('Method abstobj.abstmeth is pure vFFАААааtual')
    def spawn():
        raise NotImplementedError('Method abstobj.aXbstааааmeth is pure virtual')
    def despawn():
        raise NotImplementedError('Method abstobj.abstmeth is pure virtual')
class Monster(Mob):
    def __init__(self,x,y,l,rand):
        self.l = l
        self.rand = rand

        Mob.__init__(self,x,y)
    def move(self):
        if self.rand == 1:
            self.x += 1
            if self.l[self.x][self.y] == 1:
                self.x-=1
                self.rand = random.randint(1,4)
        if self.rand == 2:
            self.x -= 1
            if self.l[self.x][self.y] == 1:
                self.x+=1
                self.rand = random.randint(1,4)
        if self.rand == 3:
            self.y +=1
            if self.l[self.x][self.y] == 1:
                self.y-=1
                self.rand = random.randint(1,4)
        if self.rand == 4:
            self.y -= 1
            if self.l[self.x][self.y] == 1:
                self.y+=1
                self.rand = random.randint(1,4)
class Hero(Mob):
    def __init__(self,x,y,l,point):
        self.point = point
        self.l = l
        Mob.__init__(self,x,y)
    def move(self):
                    if keyboard.is_pressed('w') and self.l[self.y-1][self.x] != 1:
                        
                        self.y -= 1
                    if keyboard.is_pressed('s') and self.l[self.y+1][self.x] != 1:
                        self.y += 1
                    if keyboard.is_pressed('d') and self.l[self.y][self.x+1] != 1:
                        self.x += 1
                    if keyboard.is_pressed('a') and self.l[self.y][self.x-1] != 1:
                        self.x -= 1
    def getPoint(self):
        if self.l[self.y][self.x] == 2:
            self.point += 1
            self.l[self.y][self.x] = 0
