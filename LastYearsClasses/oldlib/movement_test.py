import time
from lib.movement import Movement
from lib.dualshock import DualShock
from lib.servo import Servo
import signal
import sys
import atexit

ps3 = DualShock()
movement = Movement()
servo1 = Servo(17)
servo2 = Servo(26)


def shutdown(signal, frame):
	print('Stopping Robot...')
	servo1.stop()
	servo2.stop()
	movement.cleanup()
	sys.exit(0)


# atexit.register(shutdown)
signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)
y = 0.00
x = 0.00

for event in ps3.controller.read_loop():
	if event.code == 02 and event.type == 3:
		x = ps3.scale_stick(event.value)
	elif event.code == 01 and event.type == 3:
		y = ps3.scale_stick(-event.value)
	if abs(y) < 20 and abs(x) < 20:
		movement.stop()
	else:
		v = (100 - abs(x)) * (y / 100) + y
		w = (100 - abs(y)) * (x / 100) + x
		r = (v + w) / 2
		l = (v - w) / 2
		movement.set_motors(l, r)
