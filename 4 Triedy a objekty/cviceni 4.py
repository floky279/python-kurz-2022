class Balik:
    def __init__(self, adresa, hmotnost): #spusti se automaticky pri vytvarani noveho objektu
        self.adresa = adresa #parameter
        self.hmotnost = hmotnost
        self.doruceno = False

    def deliver(self):
        self.doruceno = True

    def __str__(self):
        if self.doruceno is True:
            deliveredText = "balik byl dorucen"
        else:
            deliveredText = "balik nebyl dorucen"
        print(f"Adresa balika je {self.adresa}, hmotnost je {self.hmotnost} a stav dorucenia je {deliveredText}")

b1 = Balik('Petr - Praha 10',"10")
b1.__str__()

b2 = Balik('Petr - Praha 10',"10")
b2.deliver()

#2 kniha

class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena

    def discount(self, procent):
        self.cena *= 1 - (procent / 100)

    def __str__(self):
        print(f"Kniha s nazvom {self.nazev} ma pocet stran {self.pocet_stran} a cena je {self.cena}")

k = Kniha("Štastie", 350, 200)
k.discount(10)
k.__str__()
#k.__str__()
