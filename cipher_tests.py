from unittest import TestCase
import helper_functions as cipher_help


class TestCiphers(TestCase):

    def test_all_ciphers_basic(self):
        text_to_encrypt = "testing this code! 2pm"
        for cipher in cipher_help.available_ciphers:
            if cipher == "keyword":
                cipher = cipher_help.available_ciphers[cipher]("KEYWORD")
            else:
                cipher = cipher_help.available_ciphers[cipher]()

            encrypted_text = cipher.encrypt(text_to_encrypt)
            decrypted_text = cipher.decrypt(encrypted_text)
            self.assertTrue(text_to_encrypt,decrypted_text)

