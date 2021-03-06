#
#	Python library to draw information to a 128x32 PiOLED screen.
#	This library uses the Adafruit Python library for the PiOLED.
#
#	Thanks to Adafruit for the PiOLED library and the examples that
#	were used to help write this library.
#	
#	TODO:
# 		- Make aware of motor actions and errors automatically.
#		- 
#

import busio								# use for I2C
from board import SCL, SDA					# also use for I2C i think
from PIL import Image, ImageDraw, ImageFont	# working with fonts
import adafruit_ssd1306						# PiOLED library
import subprocess							# for getting IP, system load, etc.
from time import sleep						# for sleep

font = ImageFont.load_default() 			# set the font to use


# initialise display

# set the screen
display = adafruit_ssd1306.SSD1306_128_32(128, 32, busio.I2C(SCL, SDA))

width = display.width
height = display.height

image = Image.new('1', (width, height))						# create a new image

draw = ImageDraw.Draw(Image.new("1", (width, height)))
draw.rectangle((0, 0, width, height), outline=0, fill=0)	# clear the screen

# padding stuff (NOTE: Is there a way to do this more elegantly?)
padding = -2
top = padding
botton = height - padding
x = 0 	# start at the left


# main important stuff
class Screen:

	def __init__(self):
		pass

	def clearScreen(self):
		# draw a black rectangle on the screen to clear it
		draw.rectangle((0, 0, width, height), outline=0, fill=0)

	def drawIP(self, ip):
		# draw IP address
		ip_command = "hostname -I | cut -d' ' -f1"								# command to get ip address
		ip = subprocess.check_output(ip_command, shell=True).decode('utf-8')	# get ip address
		
		draw.text((x, top + 0), ip, font=font, fill=255)

	def drawSystemLoad(self):
		# draw system load
		# pasted from adafruit's cpu load example
		
		cpu_use_command = 'cut -f 1 -d " " /proc/loadavg'
		memory_use_command = "free -m | awk 'NR==2{printf \"%.2f%%\", $3,$2,$3*100/$2 }'" 

		cpu_usage = subprocess.check_output(cpu_use_command, shell=True).decode('utf-8')
		memory_usage = subprocess.check_output(memory_use_command, shell=True).decode('utf-8')

		draw.text((x, top + 8), f'CPU {cpu_usage} MEM {memory_usage}', font=font, fill=255)

	def drawDebugLine(self, text):
		# draw debug message text
		draw.text((x, top + 16), text, font=font, fill=255)

	def drawMessage(self, text):
		# draw text
		draw.text((x, top + 25), text, font=font, fill=255)

	while True:
		# NOTE: might need to change these to separate funcs and have them run
		# inside the main.py file
		# NOTE: could also have them in the init thing
		display.image(image)
		display.show()
		sleep(0.1)
