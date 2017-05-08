__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Person:

    def __init__(self):
        self.__key = ''
        self.__cipher = None
        self.__encoded = ''

    def set_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def set_encoded(self, encoded):
        self.__encoded = encoded

    def get_encoded(self):
        return self.__encoded

    def set_cipher(self, cipher):
        self.__cipher = cipher

    def get_cipher(self):
        return self.__cipher

    def operate_cipher(self):
        pass
