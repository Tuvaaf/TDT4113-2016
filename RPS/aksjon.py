

# Aksjon, 0: stein, 1: saks, 2: papir
class Aksjon:

    def __init__(self, move):
        self.move = move

    def __eq__(self, other):
        return self.move == other

    def __gt__(self, other):
        if (self.move == 0 and other == 1) or (self.move == 1 and other == 2) or (self.move == 2 and other == 0):
            return True
        return False
