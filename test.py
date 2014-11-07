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
