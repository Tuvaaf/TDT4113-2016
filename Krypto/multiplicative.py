from cipher import *
from crypto_utils import modular_inverse

from time import sleep
import random


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Multiplicative(Cipher):

    def __init__(self):
        super(Multiplicative, self).__init__()

    def encode(self, msg, key):
        encoded = ''
        for char in msg:
            char_num = (ord(char)*key - 32) % 95
            encoded += Cipher.dictionary[char_num]
        print("Sender is encrypting...")
        sleep(0.5)
        return encoded

    def decode(self, msg, key):
        decoded = ''
        m = modular_inverse(key, 95)
        for char in msg:
            char_num = ((ord(char)*m - 32) % 95)
            decoded += Cipher.dictionary[char_num]
        sleep(1)
        print("\nReceiver is decrypting...")
        sleep(0.5)
        return decoded

    def generate_keys(self):
        n = random.randint(1, 999)
        while True:
            if not modular_inverse(n, 95):
                n = random.randint(1, 999)
            else:
                return n

    def __str__(self):
        return 'Multiplicative'
