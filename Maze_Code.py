import time
import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *

speed = 100
sThreshold = int(input('Side Threshold: '))
fThreshold = int(input('Front Threshold: '))
m = Movement()

IO.setmode(IO.BCM)

Trigger = 17
l_Echo = 2
r_Echo = 3
f_Echo = 4

IO.setup(Trigger, IO.OUT)
IO.setup(l_Echo, IO.IN)
IO.setup(r_Echo, IO.IN)
IO.setup(f_Echo, IO.IN)

timetoturn90 = 2 # WILL NEED TO BE CHANGED ON DAY

while True:
  l = distance(Trigger,l_Echo)
  r = distance(Trigger,r_Echo)
  f = distance(Trigger,f_Echo)
  x=0
  
  if f > fThreshold:
    m.forward(speed,0,0)
    if x==40:
      x=0
      print(f,l,r)
  elif r < sThreshold and l > sThreshold:
    m.turn('l',0,speed)
  elif r > sThreshold and l < sThreshold:
    m.turn('r',0,speed)
  elif r > l:
    m.turn('r', 0, speed)
  else:
    m.turn('l',0,speed)

