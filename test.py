# file where i test everything

import motors
import time

motors = motors.Motors()

try:
	motors.Left.spin(20)
	motors.Right.spin(20)
	time.sleep(2000)
	motors.stop()
	
except KeyboardInterrupt:
	print("Stopping")
	motors.stop()
	motors.clean_gpio()