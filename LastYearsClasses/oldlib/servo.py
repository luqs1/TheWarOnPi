import sys
import time
import random
import pigpio
import subprocess

NUM_GPIO = 32

MIN_WIDTH = 1500
MAX_WIDTH = 2500


class Servo(object):
	def __init__(self, pin):
		# print subprocess.check_output(['sudo', 'pigpiod'])
		self.pi = pigpio.pi()

		if not self.pi.connected:
			exit()

		self.up = False
		self.cycle = 0
		self.pin = pin
		self.step = [0] * NUM_GPIO
		self.width = [0] * NUM_GPIO
		self.used = [False] * NUM_GPIO
		self.used[self.pin] = True
		self.step[self.pin] = 200
		if self.step[self.pin] % 2 == 0:
			self.step[self.pin] = -self.step[self.pin]
		self.width[self.pin] = 1500

	def move(self, val):

		# print(G, width[G])
		self.step[self.pin] = val
		self.width[self.pin] += val

		if self.width[self.pin] < MIN_WIDTH or self.width[self.pin] > MAX_WIDTH:
			self.step[self.pin] = - self.step[self.pin]
			self.width[self.pin] += self.step[self.pin]
		self.pi.set_servo_pulsewidth(self.pin, self.width[self.pin])
		time.sleep(0.1)
		return self.width[self.pin]

	def move_toggle(self, val):
		if self.cycle == 1:
			self.cycle = 0
			return False
		if self.up:
			self.step[self.pin] = val
			self.width[self.pin] += val
		else:
			self.step[self.pin] = val
			self.width[self.pin] -= val
		if self.width[self.pin] <= MIN_WIDTH:
			self.width[self.pin] = MIN_WIDTH
			self.cycle += 1
			self.up = not self.up
		elif self.width[self.pin] >= MAX_WIDTH:
			self.width[self.pin] = MAX_WIDTH
			self.cycle += 1
			self.up = not self.up
		self.pi.set_servo_pulsewidth(self.pin, self.width[self.pin])
		time.sleep(0.2)
		return True

	def reset(self):
		self.cycle = 0

	def stop(self):
		self.pi.set_servo_pulsewidth(self.pin, 0)
		self.pi.stop()
