import serial
import time

# Connects pyhon to the USB-port arduino sends signals.

class Arduino:
    def __init__(self):
        print('Initializing Arduino on serial port...')
        self.ard = serial.Serial()
        self.init_com()


    # Reads the code.
    def get_morse(self):
        return str(self.ard.readline())

    def init_com(self):
        available = False
        for comPort in range(0, 12):
            if self.try_port(comPort):
                available = True
                print ('Connection established at /dev/ttyUSB' + str(comPort) + ', please wait.')
                time.sleep(2)
                break
        if available:
            print ('Everything is OK. Listening...')


    def try_port(self, com):
        port_name = '/dev/ttyUSB' + str(com)
        try:
            global ard
            self.ard = serial.Serial(port_name, 9600, timeout=0.1)
            return True
        except:
            print(port_name + ' unavailable.')
            return False

