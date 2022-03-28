# funkce
print("Ahoj!")
print()

len([0,1,2])

round(2.34589, 3)

sum([1,2,3])
# metody
seznam = [1,2,3]
seznam.append(4)

slovnik = {'1': 'ABC'}
slovnik.items()
slovnik.values()

# definice funkce
def pozdrav():
    print("Ahoj!")

# volani funkce
pozdrav()

# definice funkce
def pozdrav(jmeno: str):
    print(f"Ahoj {jmeno}!")

# volani funkce
jmeno_uzivatele = input("Zadej tve jmeno: ")

pozdrav(jmeno_uzivatele)

# definice funkce
def pozdrav(jmeno: str):
    print(f"Ahoj {jmeno}!")
    print("Vitej u nas ve firme")

# volani funkce
jmeno_zamestnance = input("Zadej tve jmeno: ")
jmeno_manazera = input("Zadej jmeno nadrizeneho: ")

pozdrav(jmeno_zamestnance)
pozdrav(jmeno_manazera)

# varianta 1
def secti_dve_cisla(a, b):
    vysledek = a + b
    return vysledek

# varianta 2
def secti_dve_cisla(a, b):
    return a + b


vysledek_souctu = secti_dve_cisla(1, 2)
print(vysledek_souctu)

def prevod_eur_na_czk(pocet_eur: int):
    """
    Funkce prevadi eura na koruny
    s pevnym kurzem 25kc.
    """
    kurz = 25
    return pocet_eur * kurz

print(prevod_eur_na_czk(10))

# def prevod_eur_na_czk(pocet_eur, kurz=25):
def prevod_eur_na_czk(pocet_eur: int, kurz: float = 25):
    """
    Tato funkce prevadi eura na koruny .
    """
    return pocet_eur * kurz

print(prevod_eur_na_czk(pocet_eur=10, kurz=24.7))

