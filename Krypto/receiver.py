from person import Person


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Krypto"


class Receiver(Person):

    def __init__(self):
        super(Person, self).__init__()
        self.__decoded = ''

    def operate_cipher(self):
        self.set_decoded(self.get_cipher().decode(self.get_encoded(), self.get_key()))

    def get_decoded(self):
        return self.__decoded

    def set_decoded(self, decoded):
        self.__decoded = decoded
