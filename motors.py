# module for controlling the motors

import RPi.GPIO2 as GPIO	# interface with the motors

left_motor_pin = 16			# which pins to use, may need to set later
right_motor_pin = 20

left_motor_duty_cycle = 0 	# default duty cycle for the pwm
right_motor_duty_cycle = 0

pwm_frequency = 100			# frequency of the pwm (hz)

# setup
GPIO.setmode(GPIO.BCM)		# may need to set this to BOARD is stuff isn't working
GPIO.setup(left_motor_pin, GPIO.OUT) 	# pin 16 is the left motor
GPIO.setup(right_motor_pin, GPIO.OUT) 	# pin 20 is the right motor

left_motor_pwm = GPIO.PWM(left_motor_pin, pwm_frequency) 
right_motor_pwm = GPIO.PWM(right_motor_pin, pwm_frequency)

class Motors:

	# i think this is right??, unfamiliar with classes
	def __init__(self) -> None:
		pass


	def test_module(self):
		print('Module working')
		

	def stop(self):
		# stop the motors
		print('Stopping')
		left_motor_pwm.stop()
		right_motor_pwm.stop()

	def clean_gpio(self):
		# clean up the gpio
		print('Cleaning GPIO')
		GPIO.cleanup()	# resets gpio used to input

	# control left motor
	class Left:
		def __init__(self):
			pass

		def spin(self, duty_cycle):
			# spin the left motor
			print(f'Spinning left motor with duty cycle of {duty_cycle}')
			left_motor_pwm(duty_cycle)
			

		def stop(self):
			# stop the left motor
			print(f'Stopping left motor')
			left_motor_pwm.stop()

	# control right motor
	class Right:
		def __init__(self) -> None:
			pass

		def spin(self, duty_cycle):
			# spin the right motor
			print(f'Spinning right motor with duty cycle of {duty_cycle}')
			right_motor_pwm(duty_cycle)

		def stop(self):
			# stop right motor
			print(f'Stopping right motor')
			right_motor_pwm.stop()
			