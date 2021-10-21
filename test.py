# file where i test everything

import pi_vex_393	# fix this
import time

motors = pi_vex_393.Motors()

try:
	motors.Left.spin(20)
	motors.Right.spin(20)
	time.sleep(2000)
	motors.stop()
	
except KeyboardInterrupt:
	print("Stopping")
	motors.stop()
	motors.clean_gpio()