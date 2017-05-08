from cipher import Cipher
from crypto_utils import *

from random import randint


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class RSA(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()
        self.__n, self.__e = None, None

    def encode(self, msg, n_e_key):
        n1, e1 = n_e_key
        t_blocks = blocks_from_text(msg, 3)
        c = []
        for t in t_blocks:
            c.append(pow(t, e1, n1))
        return c

    def decode(self, c_blocks, n_d_key):
        n1, d1 = n_d_key
        t_blocks = []
        for c in c_blocks:
            t_blocks.append(pow(c, d1, n1))
        return text_from_blocks(t_blocks, 16)

    def generate_keys(self):
        p = generate_random_prime(16)
        q = generate_random_prime(16)
        while p == q:
            q = generate_random_prime(16)
        n1 = p*q
        phi = (p - 1) * (q - 1)
        e1 = randint(3, phi - 1)
        d1 = modular_inverse(e1, phi)

        while type(d1) == bool:
            print("KEY CRASH.\nGenerating new keys...\n")
            q = generate_random_prime(8)
            while p == q:
                q = generate_random_prime(8)
            n1 = p*q
            phi = (p - 1) * (q - 1)
            e1 = randint(3, phi - 1)
            d1 = modular_inverse(e1, phi)

        self.set_numbers((n1, e1))
        print("Keys found!\n\n")
        return n1, d1

    def set_numbers(self, keys):
        self.__n, self.__e = keys

    def get_n(self):
        return self.__n

    def get_e(self):
        return self.__e

    def __str__(self):
        return 'RSA'

"""
x = RSA()
print('********************************')
txt = 'PYT'
print('********************************')
d = x.generate_keys()
n = x.get_n()
e = x.get_e()
en = x.encode(txt, (n, e))
de = x.decode(en, (n, d))
val = x.verify(txt, de)

print('********************************')
print('Encoded: ' + str(en))
print('Decoded: ' + de)
print('********************************')
print("Valid?\t\t--->\t\t" + str(val))
"""