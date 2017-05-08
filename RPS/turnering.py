from enkeltspill import Enkeltspill
from matplotlib import pyplot as plt


class Turnering:

    # tar inne antall runder det skal spilles

    def __init__(self, spiller1, spiller2, n_games):
        self.games = n_games
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.p_spiller1 = 0
        self.p_spiller2 = 0
        self.game = 1
        self.gevinst_s1 = [0]
        self.gevinst_s2 = [0]

    def arranger_enkeltspill(self):
        game = Enkeltspill(self.spiller1, self.spiller2)
        match = game.gjennomfore_spill()
        print(str(self.game) + ": ")
        print(game)
        self.game += 1
        if match == 0:
            self.p_spiller1 += 0.5
            self.p_spiller2 += 0.5
        elif match == 1:
            self.p_spiller1 += 1
        else:
            self.p_spiller2 += 1
        self.gevinst_s1.append(self.p_spiller1/(self.game - 1))
        self.gevinst_s2.append(self.p_spiller2/(self.game - 1))

    def arranger_turnering(self):
        while self.games > 0:
            self.arranger_enkeltspill()
            self.games -= 1
        print(self)
        plt.plot(self.gevinst_s1, label=self.spiller1.navn, color='r')
        plt.plot(self.gevinst_s2, label=self.spiller2.navn, color='g')
        plt.ylim([0, 1])
        plt.ylabel("Poeng i prosent")
        plt.xlabel("Antall spill")
        plt.title(self.spiller1.navn + " vs. " + self.spiller2.navn)
        plt.legend(loc='best')
        plt.grid()
        plt.show()
    """
    def __str__(self):
        s = self.spiller1.navn + " POENG: " + str(self.p_spiller1/self.game) + "\n"
        s += self.spiller2.navn + " POENG: " + str(self.p_spiller2/self.game) + "\n"
        return s
    """

    def __str__(self):
        s1p = "{0:.2f}".format(self.p_spiller1 / self.game * 100.0)
        s2p = "{0:.2f}".format(self.p_spiller2 / self.game * 100.0)
        str1 = self.spiller1.navn + '\t\t' + s1p +'%\n'
        str2 = self.spiller2.navn + '\t' + s2p + '%\n'
        return str1 + str2

