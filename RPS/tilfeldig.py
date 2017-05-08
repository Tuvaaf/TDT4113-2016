import random

from Spiller import Spiller


class Tilfeldig(Spiller):

    def __init__(self, navn):
        Spiller.__init__(self, navn)

    def velg_aksjon(self):
        return random.randint(0, 2)
