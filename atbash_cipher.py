import string
from ciphers import Cipher


class Atbash(Cipher):

    def __init__(self, keyword=None):
        self.FORWARD = string.ascii_uppercase
        self.BACKWARD = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        """Encryption logic for the Atbash cipher.

        Arguments:
        text -- string message to encrypt.

        Returns:
        An encrypted string.
        """
        self.mode = "encrypt"
        output = []
        text = text.upper()
        for char in text:
            if char not in string.ascii_uppercase:
                output.append(char)
                continue
            index_of_letter = self.FORWARD.find(char)
            output.append(self.BACKWARD[index_of_letter])
        return "".join(output)

    def decrypt(self, text):
        """decryption logic for the Atbash cipher

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
            index_of_letter = self.BACKWARD.find(char)
            output.append(self.FORWARD[index_of_letter])
        return ''.join(output)


if __name__ == "__main__":
    atbash  = Atbash()
    encrypted_text  = atbash.encrypt("testing this code! 2pm")
    print(encrypted_text)
    decrypted_text  = atbash.decrypt(encrypted_text)
    print(decrypted_text)
