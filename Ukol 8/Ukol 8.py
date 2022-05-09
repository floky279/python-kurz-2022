from datetime import datetime

datumPredstavenia = input("Zadaj dátum predstavenia: ")
pocetOsob = input("Zadaj počet osôb: ")
pocetOsob = int(pocetOsob)
datum = datetime.strptime(datumPredstavenia, "%d. %m. %Y")
drahy_listokzac = datetime(2021, 7, 1)
drahy_listokkon = datetime(2021, 8, 10)
drahy_listok = 250
cenaDrahehoListka = pocetOsob * drahy_listok
lacny_listokzac = datetime(2021, 8, 11)
lacny_listokkon = datetime(2021, 8, 31)
lacny_listok = 180
cenaLacneholistka = pocetOsob * lacny_listok

if drahy_listokzac < datum < drahy_listokkon:
    print(f" cena listka je {cenaDrahehoListka}.")

elif lacny_listokzac < datum < lacny_listokkon:
    print(f" cena listka je {cenaLacneholistka}.")
else:
    print(f"Kino je zavrete.")
