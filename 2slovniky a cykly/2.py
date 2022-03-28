# .keys(): všetky kluce
# .values(): všetky hodnoty



sales = {                    #klic: hodnota
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for book in sales:
    if len(book) > 15:
        print(f"Titulu {book} sa predalo {sales[book]} ks.")

    print(sales.items())

for book, count in sales.items():
    if len(book) > 15:
        print(f"Titulu {book} sa predalo {sales[book]} ks.")

books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

rok = 2019

pocet_prodanych_knih = 0

for book in books:
    if book["year"] == rok:
        pocet_prodanych_knih += book["sold"]

print(f"Za rok {rok} jsme prodali {pocet_prodanych_knih} knih")

