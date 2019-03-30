from Movement import *
from Vision2 import  *
from Ultrasound import *

m = Movement()
v = Vision()
v.setmode(1)
tspeed = int(input('Turning Speed: '))
v.lamp(0,1)
area_limit = 1000
fPin = 4
trigger = 17

for i in range(2,5):
    done_colour = False
    while not done_colour:
        blocks = v.get_colour(i)
        if blocks == None:
            m.turn('r')
            print('Turning')
        else:
            print('Found Something!')
            block = blocks[0]
            x = int(block.m_x)
            y = int(block.m_y)
            a = int(block.m_width * block.m_height)
            print(block,x,y,a)
            areac = a <= area_limit
            disc = distance(trigger,fPin) > 10
            if disc:
                if abs(x -160) < 20:
                    m.forward(100,0,0)
                elif x > 160:
                    m.turn('r',0,tspeed)
                else:
                    m.turn('l',0,tspeed)
            else:
                done_colour = True