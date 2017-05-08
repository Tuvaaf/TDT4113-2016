
from Spiller import Spiller


class Test(Spiller):

    def __init__(self, name, sequence):
        Spiller.__init__(self,name)
        self.plays = sequence
        self.last_action_index = -1

    def velg_aksjon(self): # loops plays over and over
        if self.last_action_index + 1 == len(self.plays):
            self.last_action_index = 0
            return self.plays[0]
        else:
            self.last_action_index += 1
            return self.plays[self.last_action_index]

