baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
#
# Napiš program pro operátora společnosti, který poskytuje
# informaci, zda byl balík předán kurýrovi.
# Nejprve se uživatele zeptej na kód balíku.
# Následně podle hodnoty ve slovníku vypiš větu Balík byl předán kurýrovi
# nebo Balík zatím nebyl předán kurýrovi.

dorucene = input("Zadaj číslo balíku: ")
if dorucene not in baliky:
    print("Balik sa nenasiel.")
elif baliky[dorucene]:
    print(f"Balik {dorucene} je predany kurierovi.")
else:
    print(f"Balik {dorucene} nie je predany kurierovi.")

