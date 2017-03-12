from random import randrange
from util import tah

def tah_pocitace(pole, symbol_pocitace):

 # hraje xxx
 #def tah_xxx(pole):
    if "-xx" in pole:
         cislo_policka = pole.index("-xx")
         print("Počítač hraje na políčko číslo:", cislo_policka)
         return pole[:cislo_policka] + "x" + pole[cislo_policka + 1:]
    elif "xx-" in pole:
         cislo_policka = pole.index("xx-")
         print("Počítač hraje na políčko číslo:", cislo_policka)
         return pole[:cislo_policka + 2] + "x" + pole[cislo_policka + 3:]
    elif "x-x" in pole:
         cislo_policka = pole.index("x-x")
         print("Počítač hraje na políčko číslo:", cislo_policka)
         return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2:]

# obrana
    elif "xo-ox" in pole:
        cislo_policka = pole.index("xo-ox")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 2] + "x" + pole[cislo_policka + 3:]
#def tah_obrana1(pole):
    elif "-oo" in pole:
        cislo_policka = pole.index("-oo")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka] + "x" + pole[cislo_policka + 1:]
    elif "oo-" in pole:
        cislo_policka = pole.index("oo-")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 2] + "x" + pole[cislo_policka + 3:]
    elif "o-o" in pole:
        cislo_policka = pole.index("o-o")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2:]
    elif "-o-" in pole:
        cislo_policka = pole.index("-o-")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka] + "x" + pole[cislo_policka + 1:]

#def tah_xx(pole):
    elif "--x" in pole:
        cislo_policka = pole.index("--x")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2:]
    elif "x--" in pole:
        cislo_policka = pole.index("x--")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2]

# obrana x vedle o
#def tah_xo(pole):
    elif "-o" in pole:
        cislo_policka = pole.index("-o")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka] + "x" + pole[cislo_policka + 1:]
    elif "o-" in pole:
        cislo_policka = pole.index("o-")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2:]

# zahraje x---x
# def tah_x_x(pole):
    elif "x----" in pole:
        cislo_policka = pole.index("x----")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 4] + "x" + pole[cislo_policka + 5:]
    elif "----x" in pole:
        cislo_policka = pole.index("----x")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka] + "x" + pole[cislo_policka + 1:]
# zahraje x-x-x
#def tah_utok(pole):
    elif "x---x" in pole:
        cislo_policka = pole.index("x---x")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 2] + "x" + pole[cislo_policka + 3:]

# obrana - kdyz dve oo u sebe
#def tah_obrana2(pole):
    elif "o---o" in pole:
        cislo_policka =  pole.index("o---o")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 2] + "x" + pole[cislo_policka + 3:]
    elif "o--o" in pole:
        cislo_policka = pole.index("o--o")
        print("Počítač hraje na políčko číslo:", cislo_policka)
        return pole[:cislo_policka + 1] + "x" + pole[cislo_policka + 2:]

#nahodna strategie
    else:
        while True:
            if "-" not in pole:
                raise ValueError("Pole je plné.")
            cislo_policka = randrange(len(pole)) # cislo 0-19,
            print("Počítač hraje na políčko číslo:", cislo_policka)
            if pole[cislo_policka] == "-": # pokud je pole volné
                return (tah(pole,cislo_policka, symbol_pocitace))
