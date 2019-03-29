from Movement import *
from Vision2 import *
from math import *
m= Movement()
v= Vision()
v.setmode(2)
v.lamp(0,1)
while True:
    line = v.get_lowest_line()
    angle = degrees()