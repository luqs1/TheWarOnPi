import RPi.GPIO as GPIO
from time import sleep


class Movement(object):
	def __init__(self):
		# [PWM, DIGITAL]
		self._motor_pins = [[3, 5], [13, 15], [19, 21], [29, 31]]
		self._pwm_pins = []
		self._digital_pins = []
		self._digital_directions = [0, 0, 0, 0]
		self._stopped = True
		GPIO.setmode(GPIO.BOARD)
		for pwm, digital in self._motor_pins:
			GPIO.setup(digital, GPIO.OUT)
			GPIO.setup(pwm, GPIO.OUT)
			self._digital_pins.append(digital)
			self._pwm_pins.append(GPIO.PWM(pwm, 500))
		[motor.start(0) for motor in self._pwm_pins]

	def re_init(self):  # [PWM, DIGITAL]
		self._motor_pins = [[3, 5], [13, 15], [19, 21], [29, 31]]
		self._pwm_pins = []
		self._digital_pins = []
		self._digital_directions = [0, 0, 0, 0]
		self._stopped = True
		GPIO.setmode(GPIO.BOARD)
		for pwm, digital in self._motor_pins:
			GPIO.setup(digital, GPIO.OUT)
			GPIO.setup(pwm, GPIO.OUT)
			self._digital_pins.append(digital)
			self._pwm_pins.append(GPIO.PWM(pwm, 500))
		[motor.start(0) for motor in self._pwm_pins]

	def set_motors(self, left, right, time=None):
		self._stopped = False
		if -100 <= left < 0:
			self._digital_directions[0] = 0
			self._digital_directions[2] = 1
		elif left <= 100:
			self._digital_directions[0] = 1
			self._digital_directions[2] = 0
		else:
			raise Exception("Speed out of range")
		if -100 <= right < 0:
			self._digital_directions[1] = 0
			self._digital_directions[3] = 1
		elif right <= 100:
			self._digital_directions[1] = 1
			self._digital_directions[3] = 0
		else:
			raise Exception("Speed out of range")

		GPIO.output(self._digital_pins, self._digital_directions)
		for i in range(0, 2):
			self._pwm_pins[i * 2].ChangeDutyCycle(abs(left))
			self._pwm_pins[(i * 2) + 1].ChangeDutyCycle(abs(right))

		if time:
			sleep(time)
			self.stop()

	def move(self, speed, time=None):
		self.set_motors(speed, speed, time)

	def rotate(self, speed, time=None):
		# +ve = Clockwise
		# -ve = Anti-clockwise
		self.set_motors(speed, -speed, time)

	def stop(self):
		if not self._stopped:
			for x in xrange(len(self._digital_directions)):
				self._digital_directions[x] = abs(self._digital_directions[x] - 1)
			GPIO.output(self._digital_pins, self._digital_directions)
			for motor in self._pwm_pins:
				motor.ChangeDutyCycle(0)
			self._stopped = True

	def cleanup(self):
		for pin in self._digital_pins:
			GPIO.output(pin, 0)
		for motor in self._pwm_pins:
			motor.stop()
		GPIO.cleanup()

	def gpio_cleanup(self):
		GPIO.cleanup()
