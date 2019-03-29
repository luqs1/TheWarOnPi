from Movement import *
from Vision2 import *
m= Movement()
v= Vision()
v.setmode(2)
v.lamp(0,1)
while True:
    lines = v.get_