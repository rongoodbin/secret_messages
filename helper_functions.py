from atbash_cipher import Atbash
from caesar_cipher import Caesar
from keyword_cipher import Keyword
from affine_cipher import Affine
import string


available_ciphers = {"caeser": Caesar, "atbash": Atbash, "keyword": Keyword, "affine": Affine}


def lookupLetterByPos(char):

    lettermap = {number: letter for letter, number  in zip(string.ascii_uppercase, range(0,26))}
    return lettermap[char]


def lookupPosByLetter(char):

    lettermap = {letter: number for letter, number  in zip(string.ascii_uppercase, range(0,26))}
    return lettermap[char]


def remove_nonletters(text):
    str_list = []
    for char in text:
        if char not in string.ascii_uppercase:
            continue
        str_list.append(char)
    return "".join(str_list)

def getListOfPrintable():
    l = []
    for c in string.printable:
        print(c+"="+str(ord(c)))
        l.append(ord(c))
    return sorted(l)