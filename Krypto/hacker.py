from person import *
from caesar import *
from multiplicative import *
from affine import *
from unbreakable import *


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Hacker(Person):

    def __init__(self):
        super(Person, self).__init__()
        self.dic = []
        self.key = ''
        self.encoded = ''

    def hack(self, encrypted, cipher):
        self.set_dict(self.open_file())
        if isinstance(cipher, Caesar):
            return self.crack_caesar(encrypted)
        elif isinstance(cipher, Multiplicative):
            return self.crack_multi(encrypted)
        elif isinstance(cipher, Affine):
            return self.crack_affine(encrypted)
        elif isinstance(cipher, Unbreakable):
            return self.break_unbreakable(encrypted)
        else:
            print("RSA can not be cracked you twat!")

    def crack_caesar(self, enc_caesar):
        for hacker_key in range(len(Cipher.dictionary)):
            decoded = ''
            for char in enc_caesar:
                char_num = ((ord(char) - hacker_key - 32) % 95)
                decoded += Cipher.dictionary[char_num]
            decoded_words = decoded.split()
            correct_words = 0
            for word in decoded_words:
                print("Hacking word: \t\t\t" + word + " \t\t\t with key " + str(hacker_key))
                if self.word_in_dict(word.lower()):
                    correct_words += 1
                if correct_words == len(decoded_words):
                    print("********************************************************************************")
                    print("Decoded: " + decoded)
                    print("CRACKED WITH KEY " + str(hacker_key))
                    print("********************************************************************************")
                    return True
        print("********************************************************************************")
        print("The code is too strong... Could not hack.")
        return False

    def crack_multi(self, enc_multi):
        for hacker_key in range(1, 999):
            decoded = ''
            m = modular_inverse(hacker_key, 95)
            for char in enc_multi:
                char_num = ((ord(char) * m - 32) % 95)
                decoded += Cipher.dictionary[char_num]
            decoded_words = decoded.split()
            correct_words = 0
            for word in decoded_words:
                print("Hacking word:\t\t\t" + word + " \t\t\twith key\t\t\t" + str(hacker_key))
                if self.word_in_dict(word.lower()):
                    correct_words += 1
                if correct_words == len(decoded_words):
                    print("********************************************************************************")
                    print("Found a key with same modulo inverse as original key:")
                    print("Decoded: " + decoded)
                    print("CRACKED WITH KEY " + str(hacker_key))
                    print("********************************************************************************")

                    return True
        print("********************************************************************************")
        print("The code is too strong... Could not hack.")
        return False

    def crack_affine(self, enc_affine):
        for multi_key in range(1, 999):
            for caesar_key in range(len(Cipher.dictionary)):
                decoded = ''
                m = modular_inverse(multi_key, 95)
                for char in enc_affine:
                    char_num = ((ord(char) - caesar_key) * m - 32) % 95
                    decoded += Cipher.dictionary[char_num]
                decoded_words = decoded.split()
                correct_words = 0
                for word in decoded_words:
                    print("Hacking word: \t\t\t" + word + " \t\t\twith multi-key\t\t\t" + str(multi_key) +
                          " \t\tand caesar-key\t\t" + str(caesar_key))
                    if self.word_in_dict(word.lower()):
                        correct_words += 1
                    if correct_words == len(decoded_words):
                        print("********************************************************************************")
                        print("Found a key with same modulo inverse as original key: " + str(multi_key))
                        print("********************************************************************************")
                        print("Decoded:\t" + decoded)
                        print("********************************************************************************")
                        print("\nCRACKED WITH KEYS\n" + "MULTI-KEY:\t" + str(multi_key) + "\nCAESAR-KEY:\t" +
                              str(caesar_key))
                        print("********************************************************************************")
                        return True
        print("********************************************************************************")
        print("The code is too strong... Could not hack.")
        return False

    def break_unbreakable(self, enc_unb):
        for encoding_word in self.dic:
            key_decode = self.generate_decoding_key(encoding_word)
            matching_key_string = self.generate_matching_key(enc_unb, key_decode)
            decoded = ''
            for i in range(len(enc_unb)):
                char_num1 = (ord(enc_unb[i]) - 32) % 95
                char_num2 = (ord(matching_key_string[i]) - 32) % 95
                decoded += Cipher.dictionary[(char_num1 + char_num2) % 95]
            decoded_words = decoded.split()
            correct_words = 0
            for word in decoded_words:
                print("Hacking word:\t\t" + word + "\t\twith encoding-key " + str(encoding_word))
                if self.word_in_dict(word.lower()):
                    correct_words += 1
                if correct_words == len(decoded_words):
                    print("********************************************************************************")
                    print("Decoded: " + decoded)
                    print("CRACKED WITH KEYS\n" + "ENCODING KEY:\t" + str(encoding_word) + "\nDECODING KEY:\t"
                          + str(key_decode))
                    print("********************************************************************************")
                    return True
        print("********************************************************************************")
        print("The code is too strong... Could not hack.")
        return False

    def crack_rsa(self, enc_rsa):
        pass

    def word_in_dict(self, word):
        if word in self.dic:
            return True

    def set_dict(self, dic):
        self.dic = dic

    def set_key(self, key):
        self.key = key

    def set_encoded(self, encoded):
        self.encoded = encoded

    @staticmethod
    def open_file(file_path='english_words.txt'):
        file = open(file_path)
        d = []
        for line in file.readlines():
            d.append(line.split())
        file.close()
        dictionary = []
        for l in d:
            dictionary.append(l[0])
        return dictionary

    @staticmethod
    def generate_decoding_key(key_encode):
        key_decode = ''
        for char in key_encode:
            char_num = 95 - (ord(char) - 32) % 95
            key_decode += Cipher.dictionary[char_num]
        return key_decode

    @staticmethod
    def generate_matching_key(msg, keyword):
        matching_key_string = ''
        for i in range(len(msg)):
            j = i % len(keyword)
            matching_key_string += keyword[j]
        return matching_key_string

"""
h = Hacker()
h.set_dict(h.open_file())

c = Unbreakable()
key = c.generate_keys()
print("Key: " + str(key))
enc = input("Message >> ")
en = c.encode(enc, key)
print(en)

h.hack(en, c)
"""