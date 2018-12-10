import RPi.GPIO as IO # The Module that lets you control GPIO pins in the Raspberry Pi
from time import sleep
class Movement: #The Movement Class for moving the robot
    def __init__(self):
        IO.setmode(GPIO.BCM)
        self.wpins = [[18, 6], [13, 19]] #Array with sub-arrays that have to Input and Direction for both left and right
        IO.setup(self.wpins[0] + self.wpins[1], IO.OUT)
        self.left  = IO.PWM(self.wpins[0][0],100)
        self.right = IO.PWM(self.wpins[1][0],100)
    def set(self, speedl, speedr, dirl, dirr):
        self.left.start(speedl)
        self.right.start(speedr)
        IO.output(self.wpins[0][1], dirl)
        IO.output(self.wpins[1][1], dirr)
    def stop(self):
        self.set(0,0,0,0)
    def turn(self, rot, t=0, speed=100):
        if rot== 'l':
            self.set(speed,speed,1,0)
        elif rot== 'r':
            self.set(speed,speed,0,1)
        if t is not None:
            sleep(t)
            self.stop()
    def forward(self, speed, t=None):
        self.set(speed, speed, 0, 0)
        if t is not None:
            sleep(t)
            self.stop()