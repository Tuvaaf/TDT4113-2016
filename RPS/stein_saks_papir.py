from turnering import Turnering
from mestVanlig import MestVanlig
from sekvensiell import Sekvensiell
from tilfeldig import Tilfeldig
from historisk import Historisk
from tester import Test


if __name__ == "__main__":
    random1 = Tilfeldig("Random1")
    random2 = Tilfeldig("Random2")
    sek1 = Sekvensiell("Sekven1")
    sek2 = Sekvensiell("Sekven2")
    vanlig1 = MestVanlig("Vanlig1")
    vanlig2 = MestVanlig("Vanlig2")
    historisk1 = Historisk("Historisk", 3)
    historisk2 = Historisk("Historisk2", 3)

    spillere1 = [random1, sek1, vanlig1, historisk1]
    spillere2 = [random2, sek2, vanlig2, historisk2]
    print("\n--------------------------------")
    print("VELKOMMEN TIL SSP-TURNERINGEN!\n\n")
    print("\n--------------------------------")
    print("Tilfeldig:\t\t0\nSekvensiell:\t1\nMest vanlig:\t2\nHistorisk:\t\t3")
    print("\nVelg spiller 1:\n")
    i1 = int(input(">> "))
    print("\nVelg spiller 2:")
    i2 = int(input(">> "))
    print("Antall runder:\n")
    n = int(input("Runder:\n"))

    if i1 == i2:
        turnering1 = Turnering(spillere1[i1], spillere2[i2], n)
        turnering1.arranger_turnering()
    else:
        turnering2 = Turnering(spillere1[i1], spillere1[i2], n)
        turnering2.arranger_turnering()
    """"
    turneringVan = Turnering(sek1,vanlig1,100)
    turneringVan.arranger_turnering()

    turneringSek = Turnering(sek2, vanlig1, 100)
    turneringSek.arranger_turnering()

    turneringRan = Turnering(random1, random2, 100)
    turneringRan.arranger_turnering()

    turnering = Turnering(historisk2, historisk1, 100)
    turnering.arranger_turnering()
    """
