# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.

import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(r.content)
teplota = pandas.read_csv("temperature.csv")
teplota = teplota.set_index("City")
print(teplota.index)
print(teplota.info())

print(teplota.loc["Prague"])
vysoka_teplota = teplota["AvgTemperature"] > 80
print(vysoka_teplota)
teplota_europa = teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")]
print(teplota_europa[["AvgTemperature"]])

extremne_hodnoty = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)]
print(extremne_hodnoty[["AvgTemperature"]])
