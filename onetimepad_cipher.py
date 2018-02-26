import string
from ciphers import Cipher
from itertools import cycle


class OneTimepad(Cipher):

    def __init__(self):
       self.LETTERLIST = [ord(char) for char in string.ascii_uppercase]

    def encrypt(self, **kwargs):
        self.output = []
        padlist = [int(i) for i in str(kwargs["pad"])]
        text = kwargs['text'].upper()
        pool = cycle(padlist)
        for char in text:
            if char not in string.ascii_uppercase:
                self.output.append(char)
                continue
            num = next(pool)
            if "mode" in kwargs and kwargs['mode'] == "encrypt":
               index = (ord(char) + num) % len(self.LETTERLIST)
            else:
               index = (ord(char) - num) % len(self.LETTERLIST)
            charencypted = chr(self.LETTERLIST[index])
            self.output.append(charencypted)
        return "".join(self.output)

    def decrypt(self, **kwargs):
        self.encrypt(**kwargs)
        return "".join(self.output)

if __name__ == "__main__":
   cipher = OneTimepad()
   etext = cipher.encrypt(text="YEAH BABY!!",mode="encrypt", pad="1233")
   print(etext)
   dtext = cipher.encrypt(text=etext, pad="1233")
   print(dtext)
