import robot
import time

r = robot.Robot()

time.sleep(1)
r.directDrive(100, 100)
time.sleep(3)

r.directDrive(-100, -100)
time.sleep(3)

r.directDrive(100, 0)
time.sleep(5)

r.directDrive(-100, 100)
time.sleep(5)

r.directDrive(0, 0)
