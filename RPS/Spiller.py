

# en klasse som videre skal brukes for aa definere ulike typer stein,saks,papir-spillere

class Spiller:

    def __init__(self, navn):
        self.navn = navn

    # velger hvilken aksjon som skal utfroes
    def velg_aksjon(self):
        pass

    def motta_resultat(self, enkeltspill):
        pass

    def oppgi_navn(self):
        return type(self)


# Tilfeldig_spiller skal alltid velge tilfedlig mellom 0,1,2
