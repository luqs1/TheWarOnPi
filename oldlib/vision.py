from math import pi

import numpy as np
import cv2
import ast
import time
from imutils.video import VideoStream
import imutils
from pylab import array, uint8


class Vision(object):
	def __init__(self, use_pi_cam=False):
		self.camera = VideoStream(usePiCamera=use_pi_cam)
		self.bounds_file = open("./scripts/colors.txt", "r")
		self.color_info = ast.literal_eval(self.bounds_file.readline())
		self.colors = len(self.color_info)
		self.camera.start()
		time.sleep(2)

	def find_color_in_frame(self, signature, frame, show_feed, threshold=50, show_max=True):
		start = time.time()
		result = []
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)

		lower = np.array([40, 70, 70])
		upper = np.array([80, 200, 200])

		# lower = np.fromstring(self.color_info[signature]['bounds'][0][1:-1], dtype=int, sep=' ')
		# upper = np.fromstring(self.color_info[signature]['bounds'][1][1:-1], dtype=int, sep=' ')
		blurred = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(blurred, lower, upper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
		if show_feed:
			cv2.imshow(self.color_info[signature]['color'], mask)
		if len(contours) > 0:
			if show_max:
				contours = [max(contours, key=cv2.contourArea)]
			for c in contours:
				rect = cv2.minAreaRect(c)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				if cv2.contourArea(box) > threshold:
					cv2.drawContours(frame, [box], 0, (0, 0, 255), 3)
					font = cv2.QT_FONT_NORMAL
					cv2.putText(frame, self.color_info[signature]['color'], (box[0][0], box[0][1]), font, 0.5,
								(255, 255, 255), 1,
								cv2.LINE_AA)
					M = cv2.moments(box)
					cx = int(M['m10'] / M['m00'])
					cy = int(M['m01'] / M['m00'])
					result.append(
						{'area': cv2.contourArea(box), 'x': cx, 'y': cy, 'color': self.color_info[signature]['color'],
						 'time': time.time() - start})

		return frame, result

	def get_color(self, signature, show_feed=False):
		frame = self.camera.read()
		frame = imutils.resize(frame, width=400)
		frame, result = self.find_color_in_frame(signature, frame, show_feed)
		if show_feed:
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1)  #
			if key == 27:
				self.camera.stop()
				exit()
		return result

	def get_colors(self, threshold, show_feed=False):
		frame = self.camera.read()
		frame = imutils.resize(frame, width=400)
		result = []
		for x in range(0, self.colors):
			if self.color_info[x]:
				frame, cont = self.find_color_in_frame(x, threshold=threshold, frame=frame)
				result.append(cont)
		if show_feed:
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1)
			if key == 27:
				# self.camera.stop()
				exit()
		return result
