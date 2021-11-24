#!/usr/bin/env python

#
#   Vex Robotics Magnet Roomba Thing
#   
#	TODO:
#		- Figure out GPS, mapping
# 		- Move all config variables to a .json or something
#		- venv
#		- Make a webapp to control this (maybe have this one as a the backend)
#		- Object Detection (sonar, bumpers, cv, etc.)
#
#


# imports
import json

import pi_vex_393, screen

motor = pi_vex_393.Motor()
screen = screen.Screen()

