with open("auta.txt", encoding="utf-8") as vstup:
    riadky = vstup.readlines()

riadky = [riadok.split(" ") for riadok in riadky]

suma = 0.0
for riadok in riadky:
    suma += float(riadok[1].replace(",", "."))

print(suma)
