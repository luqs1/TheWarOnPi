import time
import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *

speed = 100
sThreshold = int(input('Side Threshold: '))
fThreshold = int(input('Front Threshold: '))
m = Movement()

GPIO.setmode(GPIO.BCM)

Trigger = 17
l_Echo = 2
r_Echo = 3
f_Echo = 4

IO.setup(Trigger, IO.OUT)
IO.setup(l_Echo, IO.IN)
IO.setup(r_Echo, IO.IN)
IO.setup(f_Echo, IO.IN)

while True:
  l = distance(Trigger,l_Echo)
  r = distance(Trigger,r_Echo)
  f = distance(Trigger,f_Echo)
  if f < fThreshold and r > sThreshold and l < sThreshold:
    m.turn('r','0',speed)
  elif f < fThreshold and r < sThreshold and l > sThreshold:
    m.turn('l','0',speed)
  elif f < fThreshold and r > sThreshold and l > sThreshold:
    m.turn('r','0',speed)
  else:
    m.forward(speed,0,0)
