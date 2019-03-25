import time
import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *
import time as t

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

timetoturn90 = 2 # WILL NEED TO BE CHANGED ON DAY IF USED
a = 0
x=0

while True:
  trigger(Trigger)
  l,r,f = getU(l_Echo),getU(r_Echo),getU(f_Echo)
  x+=1
  if x==30:
      x=0
      print(f,l,r, a)
  if f > fThreshold :
    if a!=1:
      m.forward(speed,0,0)
      a = 1
  elif r < sThreshold and l > sThreshold:
    if a!=2:
      m.turn('l',0,speed)
      a=2
  elif r > sThreshold and l < sThreshold:
    if a!=3:
      m.turn('r',0,speed)
      a=3
  elif r > l:
    if a!=3:
      m.turn('r', 0, speed)
      a=3
  else:
    if a!=2:
      m.turn('l',0,speed)
      a=2
