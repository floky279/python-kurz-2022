class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def get_info(self):
        print(f"{self.nazev} má {self.zanr} žáner", end="")


class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_info(self):
        super().get_info()
        print(f" a trva {self.delka} min")


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        super().get_info()
        print(f" obsahuje {self.pocet_epizod} epizod a trva {self.delka_epizody} min")


harry = Film("Harry Potter", "dobrodruzny", 150)
harry.get_info()

fringe = Serial("fringe", "sci-fi", 100, 42)
fringe.get_info()
