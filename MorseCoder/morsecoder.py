from arduinoserial import Arduino


class MorseController:

    def __init__(self):
        self.ardu = Arduino()
        self._decoded = ''
        self.word = ''
        self.symbol = ''

        self.morse_codes = {'A': '01',      'B' : '1000',   'C': '1010',    'D': '100',
                            'E': '0',       'F': '0010',    'G': '110',     'H': '0000',
                            'I': '00',      'J': '0111',    'K': '101',     'L': '0100',
                            'M': '11',      'N': '10',      'O': '111',     'P': '0110',
                            'Q': '1101',    'R': '010',     'S': '000',     'T': '1',
                            'U': '001',     'V': '0001',    'W': '011',     'X': '1001',
                            'Y': '1011',    'Z': '1100',

                            '1': '01111',   '2': '00111',   '3': '00011',   '4': '00001',
                            '5': '00000',   '6': '10000',   '7': '11000',   '8': '11100',
                            '9': '11110',   '0': '11111'}

        self.rev_morse = {v: k for k, v in self.morse_codes.items()}

        self.events = {'4': self.reset,
                       '3': self.end_word,
                       '2': self.continue_word,
                       '1': self.add_1,
                       '0': self.add_0}

        print('Initialized Morse controller')
        print('Ready for input!')
        print('0100 111 0100 = ' + self.parse_morse('0100 111 0100'))


    # Parses the event code to its coresponding character.
    def parse_morse(self, s):
        try:
            return ''.join(self.rev_morse.get(x) for x in s.split())
        except TypeError:
            print('Invalid morse...')

    # Prints event signal.
    def process_signal(self, event):
        if len(event) == 1:
            print('#', event)
            self.events[event]()

    # Processes and reads signal.
    def read_one_signal(self):
        self.process_signal(self.ardu.get_morse())

    # EVENTS
    def reset(self):
        print('RESET')
        self._decoded = ''
        self.word = ''
        self.symbol = ''

    def end_word(self):
        self._decoded += self.continue_word()
        print('Ending word. \n', self._decoded)
        self.word = ''

    def continue_word(self):
        self.word += self.symbol + ' '
        self.symbol = ''
        parsed = self.parse_morse(self.word) + ' '
        print(self.word, ':', parsed)
        return parsed

    def add_1(self):
        self.symbol += '1'

    def add_0(self):
        self.symbol += '0'

    # END EVENTS

    # Closes serial port.
    def on_close(self):
        self.ardu.ard.close()
        print('Serial connection closing..')