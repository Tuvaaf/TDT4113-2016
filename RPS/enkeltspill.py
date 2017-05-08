
from aksjon import Aksjon

# gjennomforer et enkelt spill mellom to spillere


class Enkeltspill:

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.vinner = None
        self.s1 = None
        self.s2 = None

    # returnere 0 hvis uavgjort
    # returnere 1 hvis spiller1 vinner
    # returnere 2 hvis spiller2 vinner
    def gjennomfore_spill(self):
        self.s1 = self.spiller1.velg_aksjon()  # aksjonen til spiller1
        self.s2 = self.spiller2.velg_aksjon()  # aksjonen til spiller2
        self.spiller1.motta_resultat(self)
        self.spiller2.motta_resultat(self)
        aksjon1 = Aksjon(self.s1)
        aksjon2 = Aksjon(self.s2)
        if aksjon1 == aksjon2:
            return 0
        elif aksjon1 > aksjon2:
            self.vinner = self.spiller1
            return 1
        else:
            self.vinner = self.spiller2
            return 2

    @staticmethod
    def parse_aksjon(a):
        if a == 0:
            return "Stein"
        elif a == 1:
            return "Saks"
        elif a == 2:
            return "Papir"
        else:
            return "Ukjent aksjon."

    def __str__(self):
        s1 = self.spiller1.navn + ":\t" + self.parse_aksjon(self.s1)
        s2 = self.spiller2.navn + ":\t" + self.parse_aksjon(self.s2)
        if self.vinner is None:
            return s1 + '\t\tDRAW' + '\n' + s2 + '\t\tDRAW' + '\n'
        elif self.vinner == self.spiller1:
            return s1 + '\t\tWIN' + '\n' + s2 + '\n'
        else:
            return s1 + '\n' + s2 + '\t\tWIN' + '\n'
