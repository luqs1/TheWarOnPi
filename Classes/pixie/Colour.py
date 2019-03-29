from Movement import *
from Vision2 import  *
m = Movement()
v = Vision()
v.setmode(1)
tspeed = int(input('Turning Speed: '))
v.lamp(0,1)
area_limit = int(input('Area Limit: '))
for i in range(4):
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