from morsecoder import MorseController
import time, sys


def main():

    morse = None
    try:
        morse = MorseController()
        while True:                     # Makes an everlasting loop.
            morse.read_one_signal()     # Starts process of reading morse event.
    except KeyboardInterrupt:
        sys.tracebacklimit=0            # Quits.
        print('Interrupted by you. Quitting.')
        if morse is not None:
            morse.on_close()

if __name__ == '__main__':
    main()