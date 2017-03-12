from piskvorky import vyhodnot, tah_hrace
from ai import tah_pocitace
from util import tah
from pytest import raises

# testy na vyhodnot
def test_vyhodnot_vyhral_o():
    assert vyhodnot('---ooo---') == 'o'

def test_vyhodnot_vyhral_x():
    assert vyhodnot('--xxx---') == 'x'

def test_vyhodnot_remiza():
    assert vyhodnot('xoxoxoxo') == '!'

# testy na tah
def test_tah1():
    assert tah('----',1, "x") == '-x--'
    assert tah('--x-o--', 3, "o") == '--xoo--'

def test_tah2():
    pole = tah_pocitace('--------------------',"x")
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19

# testy na tah_hrace
#def test_tah_hrace():

# testy na tah_pocitace

def test_pocitac_na_plne_pole():
    with raises(ValueError):
        assert tah_pocitace('xxoxoxox', "x")
        assert tah_pocitace('',"x")

# test - jina delka pole!
 # def test_pocitac_delka_pole():
     #assert tah_pocitace('xoxoxxooxoxxoxoxoxoox-',"o")

def test_tah_pocitace1():
    assert tah_pocitace('xo-xox', "x") == 'xoxxox'       # hraje na možné voné pole

def test_tah_pocitace2():
    assert tah_pocitace('--x--o-', "x")
    assert tah_pocitace('xx-ox',"o") == 'xxoox'
