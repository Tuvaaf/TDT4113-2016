from Spiller import Spiller
import random


class Historisk(Spiller):

    def __init__(self, name, husk):
        Spiller.__init__(self, name)
        self.alle_trekk = []
        self.husk = husk

    # saa lenge husk > len(motstander_alle_trekk) returneres det en random aksjon
    def velg_aksjon(self):
        if self.husk > len(self.alle_trekk):
            return random.randint(0, 2)
        path = self.alle_trekk[-self.husk:]
        num_moves = [0, 0, 0]  # 0: stein, 1: saks, 2: papir
        for x in range(0, len(self.alle_trekk) - self.husk):
            temp_path = self.alle_trekk[x:x + self.husk]
            index_move = x + self.husk
            if path == temp_path:
                if self.alle_trekk[index_move] == 0:
                    num_moves[0] += 1
                elif self.alle_trekk[index_move] == 1:
                    num_moves[1] += 1
                else:
                    num_moves[2] += 1
        return self.__calculate_winningmove(num_moves.index(max(num_moves)))

    @staticmethod
    def __calculate_winningmove(value):
        if value == 0:
            return 2
        elif value == 1:
            return 0
        else:
            return 1

    # finner resultatet til motstanderen og legger den til i self.mot_all_trk
    def motta_resultat(self, enkeltspill):
        if enkeltspill.spiller1 == self:
            motstander_trekk = enkeltspill.s2
        else:
            motstander_trekk = enkeltspill.s1
        self.alle_trekk.append(motstander_trekk)
