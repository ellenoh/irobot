import robot
import time

r = robot.Robot()
DELAY = 0.005

def power_pulse(delay=DELAY):
    
    for i in range(256):
        r.setPowerLED(0, i)
        time.sleep(delay)
    for i in range(255, 0, -1):
        r.setPowerLED(0, i)
        time.sleep(delay)

def power_sweep(delay=DELAY):
    for i in range(256):
        r.setPowerLED(i, 255)
        time.sleep(delay)
    for i in range(255, 0, -1):
        r.setPowerLED(i, 255)
        time.sleep(delay)

def start_stop(delay=DELAY):
    r.start()
    r.setMode(robot.SAFE)
    time.sleep(delay)
    r.directDrive(100, 100)
    time.sleep(.3)
    r.directDrive(0, 0)

def no():
    for i in range(2):
        r.directDrive(100, -100)
        time.sleep(0.3)
        r.directDrive(-100, 100)
        time.sleep(0.3)
    r.directDrive(0, 0)

def yes():
    for i in range(2):
        r.directDrive(100, 100)
        time.sleep(0.3)
        r.directDrive(-100, -100)
        time.sleep(0.3)
    r.directDrive(0, 0)

def bump_test():
    while True:
        bl, br = r.getBumpDrop()[1]
        if bl and br:
            r.setPWM(0,0)
            break
        if bl or br:
            r.setPWM(0,.2)
        time.sleep(0.015)
    power_pulse()
        
