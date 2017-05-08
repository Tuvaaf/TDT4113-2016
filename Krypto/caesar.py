from cipher import *

import random
from time import sleep


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Caesar(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()

    def encode(self, msg, key):
        encoded = ''
        for char in msg:
            char_num = (ord(char) + key - 32) % 95
            encoded += Cipher.dictionary[char_num]
        print("Sender is encrypting...")
        sleep(0.5)
        return encoded

    def decode(self, msg, key):
        decoded = ''
        for char in msg:
            char_num = ((ord(char) - key - 32) % 95)
            decoded += Cipher.dictionary[char_num]
        sleep(0.5)
        print("\nReceiver is decrypting...")
        sleep(1.5)
        return decoded

    def generate_keys(self):
        return random.randint(1, 95)

    def __str__(self):
        return 'Caesar'
