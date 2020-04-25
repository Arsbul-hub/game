from Mobs import *
from random import *
from maps import *
y = 10
x = 10
m = Monster(x,y,maps(1),randint(1,4))
h = Hero(x,y,maps(1))
while True:
    
    h.move()
    print(h.x,h.y)
#h = Hero(10,10,maps(1))
#h.move()
