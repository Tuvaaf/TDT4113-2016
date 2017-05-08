from person import Person
from rsa import RSA


class Sender(Person):

    def __init__(self):
        super(Person, self).__init__()

    def operate_cipher(self):
        message = input('Message to encrypt:\n>> ')
        print("**************************************************************************")
        if not isinstance(self.get_cipher(), RSA):
            self.set_key(self.get_cipher().generate_keys())
        self.set_encoded(self.get_cipher().encode(message, self.get_key()))
