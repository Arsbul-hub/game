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
    def getPos(self):
        return self.x,self.y
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
    def __init__(self,x,y,l,point,mi,mj):
        self.point = point
        self.l = l
        self.mi = mi
        self.mj = mj
        Mob.__init__(self,x,y)
    def move(self):
                    if keyboard.is_pressed('w') and self.l[self.y-1][self.x] != 1:
                        
                        self.mj -= 1
                    if keyboard.is_pressed('s') and self.l[self.y+1][self.x] != 1:
                        self.mj += 1
                    if keyboard.is_pressed('d') and self.l[self.y][self.x+1] != 1:
                        self.mi += 1
                    if keyboard.is_pressed('a') and self.l[self.y][self.x-1] != 1:
                        self.mi -= 1
    def collision_check(self,mpos):
        if (self.y,self.x) == mpos or mpos == (self.y,self.x):
            return True
        else:
            return False
    def getPoint(self):
        if self.l[self.y][self.x] == 2:
            self.point += 1
            self.l[self.y][self.x] = 0
    def setPoint(self):
        self.point = 0


