from Movement import *
from Vision2 import *
from math import *
m= Movement()
v= Vision()
v.setmode(2)
v.lamp(0,1)
tSpeed=30
odir=None
while True:
    line = v.get_lowest_line()
    print(line)
    if line != None:
        angle = degrees(tan((line.m_x1 -line.m_x0)/(line.m_y1 - line.m_y0 + 0.00000000001)))
        if abs(angle) < 20:
            m.forward()
        elif angle > 0:
            m.turn('r',0,tSpeed)
            odir = 'l'
        else:
            m.turn('l',0,tSpeed)
            odir = 'r'
    else:
        if odir != None:
            m.turn(odir,0,tSpeed)
