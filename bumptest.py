import robot
import time

r = robot.Robot()

r.directDrive(50, 50)
bumped = any(r.getBump())

while(True):
    print('not bumped')
    time.sleep(0.5)
    bumped = any(r.getBump())
    if bumped:
        print('bumped, so i am ending loop!')
        break
    


r.directDrive(-50, -50)
