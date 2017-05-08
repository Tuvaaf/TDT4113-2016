from cipher import *

from time import sleep


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Unbreakable(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()

    def encode(self, msg, key_encode):
        matching_key_string = self.generate_matching_key(msg, key_encode)
        encoded = ''
        for i in range(len(msg)):
            char_num1 = (ord(msg[i]) - 32) % 95
            char_num2 = (ord(matching_key_string[i]) - 32) % 95
            encoded += Cipher.dictionary[(char_num1 + char_num2) % 95]
        print("Sender is encrypting...")
        sleep(0.5)
        return encoded

    def decode(self, msg, key_encode):
        key_decode = self.generate_decoding_key(key_encode)
        matching_key_string = self.generate_matching_key(msg, key_decode)
        decoded = ''
        for i in range(len(msg)):
            char_num1 = (ord(msg[i]) - 32) % 95
            char_num2 = (ord(matching_key_string[i]) - 32) % 95
            decoded += Cipher.dictionary[(char_num1 + char_num2) % 95]
        sleep(1)
        print("\nReceiver is decrypting...")
        sleep(0.5)
        return decoded

    def generate_keys(self):
        key_encode = input("Encoding key:\n>> ").lower()
        return key_encode

    @staticmethod
    def generate_decoding_key(key_encode):
        key_decode = ''
        for char in key_encode:
            char_num = 95 - (ord(char) - 32) % 95
            key_decode += Cipher.dictionary[char_num]
        return key_decode

    @staticmethod
    def generate_matching_key(msg, key):
        matching_key_string = ''
        for i in range(len(msg)):
            j = i % len(key)
            matching_key_string += key[j]
        return matching_key_string

    def __str__(self):
        return 'Unbreakable'
