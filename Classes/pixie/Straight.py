from Movement import *
from Vision2 import *
from math import *
m= Movement()
v= Vision()
v.setmode(2)
v.lamp(0,1)
while True:
    line = v.get_lowest_line()
    if line != None:
        angle = degrees(tan((line.m_x1 -line.m_x0)/(line.m_y1 - line.m_y0)))
        if abs(angle) < 10:
            m.forward()
        elif angle > 0:
            m.turn('r')
        else:
            m.turn('l')
