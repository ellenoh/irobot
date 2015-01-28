import serial

PORTNUM = 0
BAUD = 57600
TIMEOUT = 1

class Opcode(object):
    def __init__(self, name, code, num_data=None):
        self.name = name
        self.code = code
        self.num_data = num_data


class CODES(object):
    start = Opcode('Start', 128, 0)
    safe = Opcode('Safe', 131, 0)
    full = Opcode('Full', 132, 0)
    leds = Opcode('LEDs', 139, 3)
    drive_direct = Opcode('Drive Direct', 145, 4)
    define_song = Opcode('Song', 140)
    pwm_driver = Opcode('PWM Low Side Drivers', 144, 3)
    digital_out = Opcode('Digital Outpus', 147, 1)
    low_side_drivers = Opcode('Low Side Drivers', 144, 3)
    sensor_packet = Opcode('Sensors', 142, 1)

class SENSORS(object):
    bump_drop = Opcode('Bumps and Wheel Drops', 7, 1)
    battery = Opcode('Voltage', 22, 2)
    analog_in = Opcode('Cargo Bay Analog Signal', 33, 2)


port = None

def start():
    global port
    port = serial.Serial()
    port.port = PORTNUM
    port.baudrate = BAUD
    port.timeout = TIMEOUT
    port.open()

    
def send(opcode, *args, read_num=None):
    code = opcode.code
    data = args
    if opcode.num_data is not None and (len(args) != opcode.num_data):
        raise TypeError('Command "%s" expected %d arguments, got %d' %
                        (opcode.name, opcode.num_data, len(args)))
    
    port.write([code])
    if args:
        port.write(args)

def read_sensor(sensor):
    send(CODES.sensor_packet, sensor.code)
    retval = port.read(sensor.num_data)
    return retval
    

    
