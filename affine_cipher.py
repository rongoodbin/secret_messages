import string
from ciphers import Cipher
import helper_functions as cipher_help

class Affine(Cipher):

    def encrypt(self, text):

       """
       Affine encrption uses an equation where each letter value is multiplied by 5
       and then add 8 then mod 26 as if the value is greater than 26 we loop around
       """
       output = []
       self.mode = "encrypt"
       output = []
       text = text.upper()
       for char in text:
           if char not in  string.ascii_uppercase:
               output.append(char)
               continue
           x =  cipher_help.lookupPosByLetter(char)
           cipher_value = (5*x+8)%26
           output.append(cipher_help.lookupLetterByPos(cipher_value))
       return "".join(output)


    def decrypt(self, text):

       """
       decryption for affine -  do the reverse by substracting 8 from value of letter
       multiplying by 21 then mod 26 to loop around
       """
       output = []
       self.mode = "decrypt"
       output = []
       text = text.upper()
       for char in text:
           if char not in  string.ascii_uppercase:
               output.append(char)
               continue
           x =  cipher_help.lookupPosByLetter(char)
           cipher_value = (21*(x-8))%26
           output.append(cipher_help.lookupLetterByPos(cipher_value))
       return "".join(output)


if __name__ == "__main__":
    affine  = Affine()
    encrypted_text  = affine.encrypt("Hello there Ron! Mee me at 2pm")
    print(encrypted_text)
    print(affine.decrypt(encrypted_text))
