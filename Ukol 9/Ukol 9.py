# Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.
#
# Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.
#
# Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?
#
# Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.
import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv")
open("adopce-zvirat.csv", "wb").write(r.content)

zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";")
print(zvirata.shape)
# tabulka má 513 riadkov a 6 stĺpcov

print(zvirata.columns)
#nazvy stlpcov : 'id', 'nazev_cz', 'nazev_en', 'trida_cz', 'cena', 'k_prohlidce'

print(zvirata.iloc[33,[1,2]])

# meno zvierata je v CZ: Ibis rudý v EN: Scarlet ibis
