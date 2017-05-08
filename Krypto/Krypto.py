from sender import Sender
from receiver import Receiver
from hacker import Hacker
from caesar import *
from multiplicative import *
from affine import *
from unbreakable import *
from rsa import RSA

import time


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


def main():
    s = Sender()
    r = Receiver()

    c = choose_cipher()
    if isinstance(c, RSA):
        s.set_cipher(c)
        r.set_cipher(c)
        operate_rsa(s, r)
    else:
        s.set_cipher(c)
        s.operate_cipher()
        print(s.get_encoded())

        r.set_cipher(c)
        r.set_key(s.get_key())
        r.set_encoded(s.get_encoded())

        r.operate_cipher()
        print(r.get_decoded())
        print("**************************************************************************")

        time.sleep(2)
        print("OH, NO!")
        time.sleep(0.5)
        print("A WILD HACKER APPEARED!!!")
        h = Hacker()
        h.set_key(s.get_key())
        time.sleep(1)
        print("Hacker found traces of a key...")
        h.set_encoded(s.get_encoded())
        time.sleep(1)
        print("Hacker found an encoded message...")
        h.set_dict(h.open_file())
        time.sleep(1)
        print("SHIT, he's started hacking!!!!!!")
        time.sleep(1)
        cracked = h.hack(h.encoded, s.get_cipher())
        if cracked:
            time.sleep(2)
            print("The hacker has successfully cracked your " + str(c) + " cipher algorithm.\n\\end")
        else:
            time.sleep(2)
            print("You have successfully beaten the hacker!")
            time.sleep(1)
            print("Or maybe used some words not in the dictionary...")


def choose_cipher():
    print("**************************************************************************")
    print('CHOOSE CIPHER')
    print("1: Caesar\t\t2: Multiplicative\t\t3: Affine\t\t4: Unbreakable\t\t5: RSA")
    print("**************************************************************************")
    c = str(input(">> "))
    while c.lower() not in ('1', '2', '3', '4', '5', 'c', 'm', 'a', 'u', 'r', 'cipher',
                            'multiplicative', 'affine', 'unbreakable', 'rsa'):
        print('Try again...')
        c = str(input(">> "))
    if c == '1' or c.lower() == 'cipher' or c.lower() == 'c':
        return Caesar()
    elif c == '2' or c.lower() == 'multiplicative' or c.lower() == 'm':
        return Multiplicative()
    elif c == '3' or c.lower() == 'affine' or c.lower() == 'a':
        return Affine()
    elif c == '4' or c.lower() == 'unbreakable' or c.lower() == 'u':
        return Unbreakable()
    elif c == '5' or c.lower() == 'rsa' or c.lower() == 'r':
        return RSA()


def operate_rsa(s, r):
    r.set_key(r.get_cipher().generate_keys())

    n_temp = r.get_cipher().get_n()
    e_temp = r.get_cipher().get_e()
    s.set_key((n_temp, e_temp))
    s.operate_cipher()
    print(s.get_encoded())

    r.set_encoded(s.get_encoded())
    r.operate_cipher()
    print(r.get_decoded())
    print("*************************************")


if __name__ == "__main__":
    main()
