from Classes import Movement
import keyboard
M = Movement.Movement()
def operate():
    if keyboard.is_pressed('w'):
        M.forward(50,0.1)
    elif keyboard.is_pressed('s'):
        M.stop()
    elif keyboard.is_pressed('a'):
        M.turn('l',1)
    elif keyboard.is_pressed('d'):
        M.turn('l',1)
while True:
    if keyboard.is_pressed('q'):
        break
    operate()