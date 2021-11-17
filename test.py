# file where i test everything

import pi_vex_393, screen	# fix this
import time

motors = pi_vex_393.Motors()
screen = screen.Screen()

try:
	screen.drawDebugLine('START')
	screen.drawMessage('RUNNING')

	motors.Left.spin(20)
	motors.Right.spin(20)
	screen.drawDebugLine('SPIN L AND R MTRS')
	time.sleep(2000)

	motors.stop()
	screen.drawDebugLine('STOP MTRS')
	screen.drawMessage('TASK DONE')
	

except KeyboardInterrupt:
	
	print('STOPPING')
	screen.drawMessage('KB INT')
	screen.drawDebugLine('STOPPING')

	motors.stop()
	motors.clean_gpio()