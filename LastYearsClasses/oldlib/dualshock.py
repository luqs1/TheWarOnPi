from __future__ import division
from evdev import InputDevice, categorize, list_devices
from evdev.ecodes import EV_KEY


class DualShock(object):
	def __init__(self):
		self.previous_x = 0.00
		self.previous_y = 0.00
		self.sensitivity = 100
		ps3_port = ""
		device_found = False
		for device in [InputDevice(fn) for fn in list_devices()]:
			if 'PLAYSTATION(R)3 Controller' in device.name:
				ps3_port = device.fn
				device_found = True
				break

		if device_found:
			print "Controller Ready!"
			self.controller = InputDevice(ps3_port)
		else:
			raise Exception("No Controller Found")

	def scale(self, val, src, dst):
		return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

	def scale_stick(self, value):
		return self.scale(value, (-128, 128), (-self.sensitivity, self.sensitivity))
