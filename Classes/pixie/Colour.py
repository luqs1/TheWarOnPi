from Movement import *
from Vision2 import  *
import pixy
m = Movement()
v = Vision()
v.setmode(1)
tspeed = int(input('Turning Speed: '))
pixy.set_lamp(1,0)
area_limit = 1000
for i in range(2):
    done_colour = False
    while not done_colour:
        blocks = v.get_color(i)
        if blocks == None:
            m.turn('r')
        else:
            block = blocks[0]
            x = int(block.m_x)
            y = int(block.m_y)
            a = int(block.m_width * block.m_height)
            print(block,x,y,a)
            if a <= area_limit or True:
                if abs(x -160) < 20:
                    m.forward(100,0,0)
                elif x > 160:
                    m.turn('r',0,tspeed)
                else:
                    m.turn('l',0,tspeed)
            elif a > area_limit:
                done_colour = True