import re
import requests

# Česká pošta má stránku na webu, která radí, jak správně nadepsat zásilku.
# Uvádí i několik vzorů pro české i zahraniční zásilky.
#
# V souboru posta.html nalezneš zdrojový kód této stránky v HTML (to je značkovací jazyk,
# ve kterém jsou napsané některé webové stránky, nebo části některých webových stránek.).

# Soubor si načti do proměnné tak, aby se celý jeho obsah nacházel jako jeden řetězec
# v proměnné. Můžeš využít metodu read() (doplň název souboru a název své proměnné):

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/posta.html")
open("posta.html", "wb").write(r.content)

with open("posta.html", encoding="utf-8") as vstup:
    posta = vstup.read()

posta = posta.replace("\n", "")

posta_re = re.compile(r"\d{3}\s\d{2}\s(?:[a-yA-ZÁ-Žá-ž]+\s?)+\s?\d*")
posta = posta_re.findall(posta)

print(posta)
