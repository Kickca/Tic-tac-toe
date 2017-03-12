from ai import tah_pocitace
from util import tah

def vyhodnot(pole):

    if "xxx" in pole:
        return "x"
         # vyhral hrac s x - pc
    elif "ooo" in pole:
        return "o"
         #vyhrali kolecka - hrac
    elif "-" not in pole:
        return "!" #remiza
    else:
        return "-"    # nic z toho

def vyhodnot_odpoved_hrace(pole, odpoved):
    """Pokud je odpoved hrace (retezec) spravna, vrati ji jako cislo.
    Jinak vyhodi ValueError s chybovou hlaskou.
    """
    ...
    try:
        cislo_policka = int(odpoved)
    except ValueError:
        raise ValueError("To nebylo číslo.")
    if cislo_policka < 0:
        raise ValueError("Zadej kladné číslo.")
    elif cislo_policka >= (len(pole)):
        raise ValueError("Nemůžeš hrát mimo pole.")
    elif pole[cislo_policka] != "-":
        raise ValueError("Tohle pole uz je obsazené.") # index error?
    else:
        return cislo_policka

def tah_hrace(pole):
    while True:
        odpoved = input("Kam hrat? ")
        try:
            pozice = vyhodnot_odpoved_hrace(pole, odpoved)
        except ValueError as e:
            print(e)
        else:
            return tah(pole, pozice, "o")

def piskvorky1d():
    pole = "-" * 20

    znak_hrace = "o"
    znak_pocitace = "x"
    symbol = znak_pocitace

    print("Hráč má ", znak_hrace)
    print("Počítač má", znak_pocitace)

    print(pole)
    while True:
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole, symbol)

        vysledek = vyhodnot(pole)
        if vysledek != "-": # už není volné pole
            if vysledek == "o":
                print("Vyhral jsi.")
            elif vysledek == "x":
                print("Vyhrál počítač.")
            elif vysledek == "!":
                print("Remíza.")
            break
        print(pole)
