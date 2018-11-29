import RPi.GPIO as GPIO
import time


class Ultrasonic(object):
	def __init__(self):
		self.TRIG = 32
		self.ECHO = 36
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.TRIG, GPIO.OUT)
		GPIO.setup(self.ECHO, GPIO.IN)
		GPIO.setup(self.TRIG, GPIO.OUT)
		GPIO.setup(self.ECHO, GPIO.IN)

	def distance(self):
		GPIO.output(self.TRIG, False)
		GPIO.output(self.TRIG, True)

		time.sleep(0.00001)

		GPIO.output(self.TRIG, False)
		pulse_start = None
		pulse_end = None
		while GPIO.input(self.ECHO) is 0:
			pulse_start = time.time()

		while GPIO.input(self.ECHO) is 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150

		return round(distance, 2)
