from Movement import *
from Vision2 import  *
m = Movement()
v = Vision()
areaLim = 1000
while True:
    block = v.getblock()[0]
    if block != None:
        a = block.m_height * block.m_width
        x = block.m_x
        if abs(x-160) < 30:
            m.forward()
        elif x < 160:
            m.turn('r')
        else:
            m.turn('l')
