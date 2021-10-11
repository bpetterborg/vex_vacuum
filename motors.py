# module for controlling the motors

import RPi.GPIO2 as GPIO # interface with the motors

left_motor_pin = 16		# which pins to use, may need to set later
right_motor_pin = 20

left_motor_duty_cycle = 0 			# default duty cycle for the pwm
right_motor_duty_cycle = 0

pwm_frequency = 100					# frequency of the pwm (hz)

# setup
GPIO.setmode(GPIO.BCM) # may need to set this to BOARD is stuff isn't working
GPIO.setup(left_motor_pin, GPIO.OUT) # pin 16 is the left motor
GPIO.setup(right_motor_pin, GPIO.OUT) # pin 20 is the right motor

left_motor_pwm = GPIO.PWM(left_motor_pin, pwm_frequency) 
right_motor_pwm = GPIO.PWM(right_motor_pin, pwm_frequency)

class Motors:

	# i think this is right??, unfamiliar with classes
	def __init__(self) -> None:
		pass


	def test_module(self):
		print("Module working")
		
	def forward(self, speed, distance):
		# obviously need to add the actual thing that makes the bot go brrr
		print(f"Moving forward at speed {speed}, for {distance}")

	def stop(self):
		# stop the motors
		print("Stopping")
		left_motor_pwm.stop()
		right_motor_pwm.stop()

	def clean_gpio(self):
		# clean up the gpio
		print("Cleaning GPIO")
		GPIO.cleanup()	# resets gpio used to input