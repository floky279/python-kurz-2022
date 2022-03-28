# Uvažujme vysvědčení, které máme zapsané jako slovník.
#
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

print(sum(school_report.values()) / (len(school_report.values())))

pocet = 0
soucet = 0

for key, value in school_report.items():
    soucet = soucet + value
    pocet = pocet + 1
    if value == 1:
        print(key)

print(soucet / pocet)

sumofmarks = 0
for mark in school_report.values():
    sumofmarks += mark
print(f"Priemerna znamka je {sumofmarks / len(school_report)}.")

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.- druha varianta
for x, y in school_report.items():
    if y == 1:
        print(x)
# x je key a y je value

#druha uloha
# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl.
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
#
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

hodnotenie = 8
totalpages = 0
for book in books:
  totalpages += book["pages"]
  if book["rating"] >= hodnotenie:
    print(book["title"])

print(f"Gustav celkom precital {totalpages} stran.")

print("Knihy, které hodnocení 8 a více:")
for book in books:
    if book["rating"] >= 8:
        print(book["title"])

dobre_knihy = []
pocet_dobrych_knih = 0
for book in books:
    if book["rating"] >= 8:
        pocet_dobrych_knih += 1
        dobre_knihy.append(book["title"]) #pridej na konec seznamu

#vypisanie bez zoznamu

print("\n".join(dobre_knihy))

print(pocet_dobrych_knih)

vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

#spocitame priemer pre kazdeho studenta

for student in vysledky:
  jmeno = student.pop("Jméno") #zbavime se jmena a ulozime si ho
  znamky = student.values() #znamky
  prumer = sum(znamky) / len(znamky)
  print(f"{jmeno} ma prumer znamek z maturit {prumer}")

#oddelenie cisla od mena, druha varianta
prumery = []
for student in vysledky:
  soucet_znamek = 0
  for key, value in student.items():
    if isinstance(value, int):
      soucet_znamek += value  # pricitam znamku
    else:
      jmeno = value
    prumer = soucet_znamek / 5
    print(f"{jmeno} ma prumer z maturity: {prumer}")
    prumery.append(prumer)
print(sum(prumery)/len(znamky))

# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ)
# a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele,
# jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for spz in plates:
  if spz[1] == "P":
    print(f"Majitel auta {plates[spz]} ma SPZ z Plzenskeho kraje: {spz}")








