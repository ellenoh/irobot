import robot
import time

r = robot.Robot()

def driveA_C():
    r.directDrive(100, 100)
    time.sleep(24)
    jingle_bells = [64, 12, 64, 12, 64, 24, 64, 12,
                    64, 12, 64, 24, 64, 12, 67, 12,
                    60, 12, 62, 12, 64, 24]
    r.defineSong(3, jingle_bells)
    r.playSong(3)

    r.directDrive(-100, 100)
    time.sleep(2)

    r.directDrive(100, 100)
    time.sleep(18)

    r.directDrive(0, 0)

"""
if start == 'C' and end == 'A':
 
    r.directDrive(100, 100)
    time.sleep(18)
    
    jingle_bells = [64, 12, 64, 12, 64, 24, 64, 12,
                    64, 12, 64, 24, 64, 12, 67, 12,
                    60, 12, 62, 12, 64, 24]
    r.defineSong(3, jingle_bells)
    r.playSong(3)

    r.directDrive(100, -100)
    time.sleep(2)

    r.directDrive(100, 100)
    time.sleep(24)

    r.directDrive(0, 0)
"""

print ("What is your starting point?")
start = input()
print ("What is your end point?")
end = input()

if start == 'A' and end == 'C':
    driveA_C()
