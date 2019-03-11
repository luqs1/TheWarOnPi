import time
import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *

speed = 100
threshold = 20
m = Movement()

GPIO.setmode(GPIO.BCM)

l_Trigger = 0
l_Echo = 0
r_Trigger = 0
l_Echo = 0
f_Trigger = 0
f_Echo = 0

IO.setup(l_Trigger, IO.OUT)
IO.setup(l_Echo, IO.IN)
IO.setup(r_Trigger, IO.OUT)
IO.setup(r_Echo, IO.IN)
IO.setup(f_Trigger, IO.OUT)
IO.setup(f_Echo, IO.IN)

l = distance(l_Trigger,l_Echo)    # need to add arguments to Ultrasound class
r = distance(r_Trigger,r_Echo)
f = distance(f_Trigger,f_Echo)

while True:
  if f < threshold and r > threshold and l < threshold:
    m.turn('r','0',speed)
  elif f < threshold and r < threshold and l > threshold:
    m.turn('l','0',speed)
  elif f < threshold and r > threshold and l > threshold:
    m.turn('r','0',speed)
  else:
    m.forward(speed,0,1)
