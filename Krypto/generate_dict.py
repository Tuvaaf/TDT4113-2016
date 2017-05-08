__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


def generate_dict():
    start = 32
    stop = 127
    d = {}
    i = 0
    for c in range(start, stop):
        d[i] = chr(c)
        i += 1
    return d