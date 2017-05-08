from Spiller import Spiller
import random


class Sekvensiell(Spiller):

    def __init__(self, navn):
        Spiller.__init__(self, navn)
        self.prev_aksjon = random.randint(0, 2)  # Tilfeldig start

    def velg_aksjon(self):
        if self.prev_aksjon == 0:
            next_aksjon = 1
        elif self.prev_aksjon == 1:
            next_aksjon = 2
        else:
            next_aksjon = 0
        self.prev_aksjon = next_aksjon
        return next_aksjon
