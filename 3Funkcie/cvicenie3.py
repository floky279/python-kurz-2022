# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
    return a * b


print(mult(5, 7))

# Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu.
# Parametr breakfast je nepovinný a výchozí hodnota je False.
#
# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(persons, breakfast=False):
    if breakfast is True:
        price = (persons * 850)+125
    else:
        price = persons * 850
    return price

print(total_price(3, True))

#druha verzia
def total_price(persons, breakfast=False):
    pricePerPerson = 850
    if breakfast is True:
        pricePerPerson += 125
    return pricePerPerson * persons

print(total_price(3))
print(total_price(3, True))

# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň,
# že pro ženy je k měsíci připočtena hodnota 50.
#
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def month_of_birth(rodne_cislo):
    cislo_mesice = int(str(rodne_cislo)[2:4])
    if cislo_mesice <= 12:
        return cislo_mesice
    else:
        return cislo_mesice - 50

print(f'9207054439 -> {month_of_birth(9207054439)}')
print(f'9555125899 -> {month_of_birth(9555125899)}')
print(month_of_birth("9107306762"))

