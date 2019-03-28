from Classes.Movement import *
from Classes.Vision2 import  *
m = Movement()
v = Vision()
area_limit = 1000
for i in range(4):
    done_colour = False
    while not done_colour:
        blocks = v.get_colour(i)
        if blocks == None:
            m.turn('r')
        for block in blocks:
            x = block.m_x
            y = block.m_y
            a = block.m_width * block.m_height
        if a <= area_limit:
            if abs(x-200) <= 30:
                m.forward(20)
            elif x > 200:
                m.turn('r')
            else:
                m.turn('l')
        elif a > area_limit:
            done_colour = True