# file where i test everything

import pi_vex_393, screen	# fix this
import time

motor = pi_vex_393.Motor()
screen = screen.Screen()


	
while True:

	screen.clearScreen()
	screen.drawIP()
	screen.drawSystemLoad()
	screen.drawDebugLine(motor.currentStatus())

	try:	
		motor.spin('left', 50)
		motor.spin('right', 50)

	except KeyboardInterrupt:
		motor.stop('left')
		motor.stop('right')