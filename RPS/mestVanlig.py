from Spiller import Spiller
import random


# mest_vanlig_spiller maa motta resultatene til motspilleren for aa avgjore
# hvilket trekk det neste er
class MestVanlig(Spiller):

    def __init__(self,navn):
        Spiller.__init__(self, navn)
        #super(Mest_vanlig_spiller, self).__init__(navn)
        self.motstander_alletrekk = [0,0,0] # p1 = stein p2 = saks p3 = papir

    def velg_aksjon(self):
        max_trekk = self.motstander_alletrekk.index(max(self.motstander_alletrekk))
        if self.motstander_alletrekk[0] == self.motstander_alletrekk[1] == self.motstander_alletrekk[2]:
            return random.choice([0,1,2])
        elif max_trekk == self.motstander_alletrekk[0] == self.motstander_alletrekk[1]:
            return random.choice([0,1])
        elif max_trekk ==self.motstander_alletrekk[0] == self.motstander_alletrekk[2]:
            return random.choice([0,2])
        elif max_trekk==self.motstander_alletrekk[1] ==self.motstander_alletrekk[2]:
            return random.randint(1,2)
        else:
            return max_trekk

    # tar inn et enkeltspill og finner trekket til motsanderen
    def motta_resultat(self,enkeltspill):
        if enkeltspill.spiller1 == self:
            motstander_trekk = enkeltspill.s2
        else:
            motstander_trekk = enkeltspill.s1
        if motstander_trekk == 0:
            self.motstander_alletrekk[0]+=1
        elif motstander_trekk == 1:
            self.motstander_alletrekk[1]+=1
        else:
            self.motstander_alletrekk[2]+=1