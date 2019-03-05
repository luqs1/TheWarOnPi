#Interactive Movement using a Keyboard!!! JUST DEWITT!!!
from Classes import Movement
import keyboard
M = Movement.Movement()
"""
class test:
    def __init__(self):
        pass
    def forward(self,*args):
        print('FORWARDS')
    def stop(self):
        print('STOP')
    def turn(self, letter, *args):
        print('TURNING',letter)
#M = test()
"""

def operate(arg):
    if arg.name == 'w'      : M.forward(50,0.1)
    elif arg.name == 's'    : M.stop()
    elif arg.name == 'a'    : M.turn('l',1)
    elif arg.name == 'd'    : M.turn('r',1)
keyboard.on_press(operate)
keyboard.wait('q')