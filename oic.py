import serial

PORTNUM = 0
BAUD = 57600

class Opcode(object):
    def __init__(self, name, code, num_data=0, desc=''):
        self.name = name
        self.code = code
        self.num_data = num_data
        self.description = desc

class CODES(object):
    start = Opcode('Start', 128, 0)
    safe = Opcode('Safe', 131, 0)
    full = Opcode('Full', 132, 0)
    leds = Opcode('LEDs', 139, 3)
    drive_direct = Opcode('Drive Direct', 145, 4)

port = None

def start():
    global port
    port = serial.Serial()
    port.port = PORTNUM
    port.baudrate = BAUD
    port.open()

    
def send(opcode, *args):
    code = opcode.code
    data = args
    if len(args) != opcode.num_data:
        raise TypeError('Command "%s" expected %d arguments, got %d' %
                        (opcode.name, opcode.num_data, len(args)))
    
    port.write([code])
    if args:
        port.write(args)
