import string
from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self, keyword):
        
        self.keyword = keyword.upper()
        self.FORWARD = string.ascii_uppercase
        self.setup_mono()

    def setup_mono(self):
        """
        setup alphabet with keyword added in the beginning of the alphabet.
        This is done by removing letters that are in the keyword and then appending
        the keyword  to the letter list
        """
        self.monoalphabet = [char for char in string.ascii_uppercase]
        for letter in self.keyword:
            try:
               self.monoalphabet.remove(letter)
            except:
                pass
        self.monoalphabet =  self.keyword.upper() + "".join(self.monoalphabet)


    def encrypt(self, text):
        """Encryption logic for the keyword cipher.

        Arguments:
        text -- string message to encrypt.

        Returns:
        An encrypted string.
        """
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
        """decryption logic for the keyword cipher


        Arguments:
        text -- string message to decrypt.

        Returns:
        Decrypted string.
        """
        output = []
        text = text.upper()
        for char in text:
            if char not in string.ascii_uppercase:
                output.append(char)
                continue
            index_of_letter = self.monoalphabet.find(char)
            output.append(self.FORWARD[index_of_letter])
        return ''.join(output)

