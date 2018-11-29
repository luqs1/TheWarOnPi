#import RPi.GPIO as IO # The Module that lets you control GPIO pins in the Raspberry Pi
class Movement: #The Movement Class for moving the robot
    def __init__(self):
        IO.setmode(GPIO.BCM)
        self.wheelpins = [[0,1],[2,3]] #Array with sub-arrays that have to Input and Direction for both left and right
        self.register(self.allpins[0]+self.allpins[1]) #function for registering the pins as in/output (and pwm)
    def register(self, pins, mode):
        if mode == 'OUTPUT':
            type = IO.OUTPUT
        elif mode == 'INPUT':
            type = IO.INPUT
        else:
            type = IO.OUTPUT
        for pin in pins:
            IO.setup(pin, type)

m = Movement()
print(m.allpins)