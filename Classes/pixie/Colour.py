from Movement import *
from Vision2 import  *
import pixy
m = Movement()
v = Vision()
pixy.set_lamp(1,0)
area_limit = 1000
for i in range(2):
    done_colour = False
    while not done_colour:
        blocks = v.get_block()
        if blocks == None:
            m.turn('r')
        else:
            block = blocks[0]
            x = block.m_x
            y = block.m_y
            a = block.m_width * block.m_height
            print(block,x,y,a)
            if a <= area_limit or True:
                if x < 160:
                    m.forward(100,0,0)
                elif x > 160:
                    m.turn('r')
                else:
                    m.turn('l')
            """
            elif a > area_limit:
                done_colour = True
            """