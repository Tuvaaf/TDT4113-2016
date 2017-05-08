from cipher import *
from crypto_utils import modular_inverse

import random
from time import sleep


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Affine(Cipher):

    def __init__(self):
        super(Affine, self).__init__()
        self.__key2 = random.randint(0, 95)

    def encode(self, msg, key1):
        encoded = ''
        for char in msg:
            char_num = (ord(char)*key1 + self.__key2 - 32) % 95
            encoded += Cipher.dictionary[char_num]
        print("Sender is encrypting...")
        sleep(0.5)
        return encoded

    def decode(self, msg, key1):
        decoded = ''
        m = modular_inverse(key1, 95)
        for char in msg:
            char_num = ((ord(char)-self.__key2)*m - 32) % 95
            decoded += Cipher.dictionary[char_num]
        sleep(1)
        print("\nReceiver is decrypting...")
        sleep(0.5)
        return decoded

    def generate_keys(self):
        n = random.randint(1, 999)
        crashes = 0
        while True:
            if not modular_inverse(n, 95):
                crashes += 1
                n = random.randint(1, 999)
                print("Keys crashing...")
            else:
                if crashes > 0:
                    print("Problem dealt with.")
                return n

    def get_key2(self):
        return self.__key2

    def __str__(self):
        return 'Affine'
