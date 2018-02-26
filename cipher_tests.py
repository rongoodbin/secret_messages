from unittest import TestCase
import helper_functions as cipher_help
from onetimepad_cipher import OneTimepad

"""
This class performs tests on the various ciphers that I have implemented
"""
class TestCiphers(TestCase):

    """
    Perform basic tests of all ciphers. Ensure text to encrypt is encrypted and then decrypted back to orginal text
    """
    def test_all_ciphers_basic(self):
        text_to_encrypt = "TESTING THIS CODE! 2PM"
        for cipher in cipher_help.available_ciphers:
            if cipher == "keyword":
                cipher = cipher_help.available_ciphers[cipher]("KEYWORD")
            else:
                cipher = cipher_help.available_ciphers[cipher]()

            encrypted_text = cipher.encrypt(text_to_encrypt)
            decrypted_text = cipher.decrypt(encrypted_text)
            self.assertEquals(text_to_encrypt,decrypted_text)

    def test_all_ciphers_with_onetimepad(self):
        """
        Perform same tests above and add in one time pad. Ensure text to encrypt is encrypted and then decrypted back to orginal text
        """
        onetimepad = OneTimepad()
        text_to_encrypt = "HELLO THERE MARRY JANE"
        pad = "12345"
        for cipher in cipher_help.available_ciphers:
            if cipher == "keyword":
                cipher = cipher_help.available_ciphers[cipher]("KEYWORD")
            else:
                cipher = cipher_help.available_ciphers[cipher]()

            encrypted_text = cipher.encrypt(text_to_encrypt)
            encrypted_message_padded = onetimepad.encrypt(text=encrypted_text, mode="encrypt", pad=pad)
            decrypted_message_padded = onetimepad.decrypt(text=encrypted_message_padded, mode="decrypt", pad="12345")
            decrypted_text = cipher.decrypt(decrypted_message_padded)
            self.assertEqual(text_to_encrypt,decrypted_text)