from atbash_cipher import Atbash
from caesar_cipher import Caesar
from keyword_cipher import Keyword
from affine_cipher import Affine
import string
import random

available_ciphers = {"caeser": Caesar, "atbash": Atbash, "keyword": Keyword, "affine": Affine}
extracharlist = ["%", "^", "*", "&", "#"]


"""
Given a letter, get the number's position from 0-25
"""
def lookupLetterByPos(char):

    lettermap = {number: letter for letter, number  in zip(string.ascii_uppercase, range(0,26))}
    return lettermap[char]


"""
Given a position, get the letter 
"""
def lookupPosByLetter(char):

    lettermap = {letter: number for letter, number  in zip(string.ascii_uppercase, range(0,26))}
    return lettermap[char]


"""
return a new string of all ASCI characters only, removing a
non ascii characters.
"""
def remove_nonletters(text):
    str_list = []
    for char in text:
        if char not in string.ascii_uppercase:
            continue
        str_list.append(char)
    return "".join(str_list)

"""
:return a sorted list of ord(c) values 
"""
def getListOfPrintable():
    l = []
    for c in string.printable:
        l.append(ord(c))
    return sorted(l)

"""
:return the message in blocks of 5. append special characters in case string
is not divisable by 5. replace any spaces with "_"
"""
def blocksoffive_encrypt(message):
    message = str.replace(message," ","_")
    output = []
    blocksof = 5
    charsmissing = blocksof - (len(message)%blocksof)
    strl = [c for c in message]
    for _ in range(charsmissing):
        extrachar = random.choice(extracharlist)
        strl.append(extrachar)
    blocklist = [strl[i:i + blocksof] for i in range(0, len(strl), blocksof)]
    for block in blocklist:
        output.append("".join(block))

    return " ".join(output)

"""
:return the message reassembled back from blocks of 5
"""
def blocksoffive_decrypt(message):
    message = str.replace(message," ","")
    message = str.replace(message,"_"," ")
    output = []
    for char in message:
        if char in extracharlist:
           break
        output.append(char)
    return "".join(output)