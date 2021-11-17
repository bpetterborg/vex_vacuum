#
#	This is where the fun object detection stuff happens.
#	I am doing this to put OpenCV on my resume.
#	
#	Uses OpenCV to detect objects from the camera attached
#	to the RPi's CSI port.
#
#	TODO:
#		- Lots of testing
#		- Finish this
#
#

# imports
import cv2								# object detection
from picamera.array import PiRGBArray	# pi camera 
from picamera import PiCamera			# pi camera
import numpy as np						# numpy


# main stuff
class Vision:
	def __init__(self):
		pass

	def version(self):
		return cv2.__version__

	