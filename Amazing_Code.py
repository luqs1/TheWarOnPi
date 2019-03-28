import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *
import time as t
 
speed = 100
sleeptime = float(input('Delay: '))
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
        t.sleep(sleeptime / 2)
        aRight = distance(Trigger, r_Echo)
        if aRight < reasonableValueMark:
            totalRight.append(aRight)
        t.sleep(sleeptime / 2)
        aFront = distance(Trigger, f_Echo)
        if aFront < reasonableValueMark:
            totalFront.append(aFront)
    if 0 not in [len(totalFront),len(totalLeft),len(totalRight)]:
        averageLeft = sum(totalLeft)/len(totalLeft)
        averageRight = sum(totalRight)/len(totalRight)
        averageFront = sum(totalFront)/len(totalFront)
    else:
        averageFront=0
        averageRight=0
        averageLeft=0
    print(averageLeft,averageRight,averageFront)
 
    if averageFront > fThreshold:
        m.forward(speed, 0, 0)
    elif averageRight > sThreshold and averageLeft < sThreshold:
        m.turn('r', 0, speed)
    elif averageRight < sThreshold and averageLeft > sThreshold:
        m.turn('l', 0, speed)
    elif averageRight > averageLeft:
        m.turn90('r',100)
    elif averageLeft > averageRight:
        m.turn90('l',100)
    else:
        m.stop()
       
    # Fire that Never Seven times!
