# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který
# provede následující činnosti:
#
# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:
#
# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být
# devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420").
# Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky.
# To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
# vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.


# Nápověda
# Pokud chcete zkontrolovat předvolbu, stačí využít podmínku+420 in cislo,
# alternativně můžete využít indexy: Python umožňuje kromě jednoho znaku z řetězce získat
# i více znaků, a to pomocí dvojtečky. Pokud budete chtít získat první čtyři znaky,
# napište cislo[0:4]. Pak můžete vytvořit podmínku cislo[0:4] == "+420".
import math


def send_text_message():
    number = input("Zadaj telefonne cislo:")
    if validate_phone_number(number):
        text_message = input("Zadaj text správy:")
        print(f"Cena Vašej spravy je {message_price(text_message)} Kc.")
    else:
        print("Neplatné telefonne číslo.")


def validate_phone_number(number):
    number = number.replace(" ", "")
    return len(number) == 9 or len(number) == 13


def message_price(message):
    length = len(message)
    if length == 0:
        return 3
    return math.ceil(length/180) * 3


send_text_message()
