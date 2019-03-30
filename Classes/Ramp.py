import RPi.GPIO as IO
from time import sleep

class Ramp:
    def __init__(self):
        IO.setmode(IO.BCM)
        self.elevatePin = 23
        self.descendPin = 24
        IO.setup([self.elevatePin,self.descendPin],IO.OUT)
    def angleup(self):
        IO.output(self.elevatePin,1)
    def angledown(self):
        IO.output(self.descendPin,1)
    def anglestop(self):
        IO.output(self.elevatePin,0)
        IO.output(self.elevatePin,0)