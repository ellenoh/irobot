import oic
from oic import CODES, SENSORS

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

    def reset(self):
        self.setDefaults()

    def setDefaults(self):
        self.setMode(FULL)
        self.led_state = [0, 0, 0]
        self.pwm_state = [0, 0, 0]
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

    def playSong(self, song_number):
        oic.port.write([141, song_number])

    def defineSong(self, song_number, note_list):
        song_length = int(len(note_list)/2)
        l = [140, song_number, song_length]
        l2 = l + note_list
        oic.port.write(l2)

    def getBumpDrop(self):
        retval = oic.read_sensor(SENSORS.bump_drop)
        byte = retval[0]
        wheel_drop_castor = get_bit(byte, 4)
        wheel_drop_left = get_bit(byte, 3)
        wheel_drop_right = get_bit(byte, 2)
        bump_left = get_bit(byte, 1)
        bump_right = get_bit(byte, 0)
        return ((wheel_drop_castor, wheel_drop_left, wheel_drop_right),
                (bump_left, bump_right))

    def getBump(self):
        retval = self.getBumpDrop()
        return retval[1]

    def getBatteryVoltage(self):
        retval = oic.read_sensor(SENSORS.battery)
        voltage = (retval[0]*256 + retval[1])/1000
        return voltage

    def getAnalogIn(self):
        retval = oic.read_sensor(SENSORS.analog_in)
        voltage = (retval[0]*256 + retval[1])*5/1023
        return voltage

    def setPWM(self, chan, fraction):
        if chan not in (0, 1, 2):
            raise ValueError('There is no PWM %d' % chan)
        if fraction > 1 or fraction < 0:
            raise ValueError('Invalid fraction: %f' % fraction)
        self.pwm_state[chan] = int(fraction * 128)
        print(self.pwm_state)
        oic.send(CODES.low_side_drivers, self.pwm_state[2],
                 self.pwm_state[1], self.pwm_state[0])
        
               
def get_bit(val, pos):
    return bool(val & (1<<pos))
       
def int_to_bytes(val):
    if val >= 0x8000 or val <= -0x8000:
        raise ValueError('Value must be between -32767 and 32767')
    if val < 0:
        val += 0xFFFF
    return val >> 8, val & 0xFF
