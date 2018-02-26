import string

from ciphers import Cipher

class Caesar(Cipher):

    FORWARD = string.ascii_uppercase * 3

    def __init__(self, keyword=None, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)


if __name__ == "__main__":
    atbash  = Caesar()
    encrypted_text  = atbash.encrypt("testing this code! 2pm")
    print(encrypted_text)
    decrypted_text  = atbash.decrypt(encrypted_text)
    print(decrypted_text)
