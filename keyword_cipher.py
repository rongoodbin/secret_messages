import string
from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self, keyword):
        
        self.keyword = keyword.upper()
        self.FORWARD = string.ascii_uppercase
        self.setup_mono()

    def setup_mono(self):
        self.monoalphabet = [char for char in string.ascii_uppercase]
        for letter in self.keyword:
            try:
               self.monoalphabet.remove(letter)
            except:
                pass
        self.monoalphabet =  self.keyword.upper() + "".join(self.monoalphabet)


    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            if char not in string.ascii_uppercase:
                output.append(char)
                continue
            index_of_letter = self.FORWARD.find(char)
            output.append(self.monoalphabet[index_of_letter])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            if char not in string.ascii_uppercase:
                output.append(char)
                continue
            index_of_letter = self.monoalphabet.find(char)
            output.append(self.FORWARD[index_of_letter])
        return ''.join(output)

if __name__ == "__main__":
    keyword  = Keyword("kryptos")
    encrypted_text  = keyword.encrypt("KNOWLEDGE  IS  POWER! MEET @2pm")
    print(encrypted_text)
    decrypted_text  = keyword.decrypt(encrypted_text)
    print(decrypted_text)

