import oic
CODES = oic.CODES
PASSIVE, SAFE, FULL = 'passive', 'safe', 'full'

class Robot(object):
    def __init__(self):
        oic.start()
        self.led_state = None
        self.mode = None
        self.start()
        self.setDefaults()

    def start(self):
        oic.send(CODES.start)
        self.mode = PASSIVE

    def setMode(self, mode):
        if mode == PASSIVE:
            self.start()
        elif mode == SAFE:
            oic.send(CODES.safe)
        elif mode == FULL:
            oic.send(CODES.full)
        else:
            return
        self.mode = mode

    def mode():
        return self.mode

    def setDefaults(self):
        self.setMode(SAFE)
        self.led_state = [0, 0, 0]
        self.updateLEDState()
        
    def setPowerLED(self, color, intensity):
        self.led_state[1] = color
        self.led_state[2] = intensity
        self.updateLEDState()

    def updateLEDState(self):
        oic.send(CODES.leds, *self.led_state)

    def playLEDState(self):
        return self.led_state[0] & 2

    def advanceLEDState(self):
        return self.led_state[0] & 8

    def setPlayLED(self, enable):
        state = self.advanceLEDState()
        if enable:
            state += 2
        self.led_state[0] = state
        self.updateLEDState()

    def setAdvanceLED(self, enable):
        state = self.playLEDState()
        if enable:
            state += 8
        self.led_state[0] = state
        self.updateLEDState()

    def directDrive(self, left_vel, right_vel):
        left_high, left_low = int_to_bytes(left_vel)
        right_high, right_low = int_to_bytes(right_vel)
        oic.send(CODES.drive_direct, right_high, right_low,
                 left_high, left_low)


def int_to_bytes(val):
    if val >= 0x8000 or val <= -0x8000:
        raise ValueError('Value must be between -32767 and 32767')
    if val < 0:
        val += 0xFFFF
    return val >> 8, val & 0xFF
