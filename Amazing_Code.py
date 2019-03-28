import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *
import time as t
 
speed = 100
sThreshold = int(input('Side Threshold: '))
fThreshold = int(input('Front Threshold: '))
reasonableValueMark = int(input('Ultrasound Distance Limit: ')) #
 
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
 
timetoturn90 = 2  # WILL NEED TO BE CHANGED ON DAY IF USED
 
while True:
    totalLeft, totalRight, totalFront = [], [], []
 
    for counter in range(10):
        aLeft = distance(Trigger, l_Echo)
        if aLeft < reasonableValueMark:
            totalLeft.append(aLeft)
 
        aRight = distance(Trigger, r_Echo)
        if aRight < reasonableValueMark:
            totalRight.append(aRight)
 
        aFront = distance(Trigger, f_Echo)
        if aFront < reasonableValueMark:
            totalFront.append(aFront)
 
        t.sleep(0.100)
 
    averageLeft = sum(totalLeft)/len(totalLeft)
    averageRight = sum(totalRight)/len(totalRight)
    averageFront = sum(totalFront)/len(totalFront)
 
    if averageFront > fThreshold:
        m.forward(speed, 0, 0)
    elif averageRight > sThreshold and averageLeft < sThreshold:
        m.turn('r', 0, speed)
    elif averageRight < sThreshold and averageLeft > sThreshold:
        m.turn('l', 0, speed)
    elif averageRight > averageLeft:
        m.turn('r', 0, speed)
    elif averageLeft > averageRight:
        m.turn('l', 0, speed)
       
    # Fire that Never Seven times!
