class Auto:
    def __init__(self, registracna_znacka, znacka_vozidla, pocet_km):
        self.registracna_znacka = registracna_znacka
        self.znacka_vozidla = znacka_vozidla
        self.pocet_km = pocet_km
        self.volne = True

    def puj_auto(self):
        self.volne = True

    def __str__(self):
        if self.volne is True:
            print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici")

    def get_info(self):
        if pozicanie == "peugeot":
            print(f"{self.registracna_znacka} {self.znacka_vozidla}")
        elif pozicanie == "škoda":
            print(f"{self.registracna_znacka} {self.znacka_vozidla}")
        else:
            print(f"Neexistujúce auto")


pozicanie = input("Vyberte typ auta:")


peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
peugeot.get_info()
peugeot.__str__()
škoda = Auto("1P3 4747", "Škoda Octavia", "41253")
škoda.get_info()
peugeot.__str__()

