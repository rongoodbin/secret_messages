import helper_functions as cipher_help
import os
from onetimepad_cipher import OneTimepad
import sys

dash = "-"
available_ciphers_text = "These are the current available ciphers:\n"
newline = os.linesep

"""
show the user all available ciphers
"""
def showAvailableCiphers():
    print(available_ciphers_text)
    for cipher in cipher_help.available_ciphers:
        print(dash + cipher)

"""
Launch point is here in main()  - interact with the user. get the cipher they 
want to use and message to encrypt/decrypt.
Added in one time pad for extra security, in which case a number is requested 
from the user. Note, that with the one time pad. We perform the one time pad 
on encrypted text when encrypting and one time pad decryption is performed 
before decrypting using the selected cipher.
"""
def main():
    welcome_text  = "This is the secret messages project for the Treehouse " \
                    "techdegree."+newline
    print(welcome_text)
    keyword = None
    inWhileLoop = False
    showAvailableCiphers()
    cipher_from_user = input("\nWhich cipher would you like to use?: ")
    if cipher_from_user in cipher_help.available_ciphers.keys():
            if cipher_from_user == "keyword":
               keyword = input("Keyword cipher is a fantastic cipher. Please enter a keyword to use?")
               str_from_user = input("What is the message?" + newline)

            else:
               str_from_user = input("That is a fantastic cipher. "\
                                     "What is the message?"+newline)
            while True:
                    if inWhileLoop:
                        somethingelse = input("encrypt/decrypt something "\
                                          "else? y/n:")
                        if somethingelse == "n":
                            sys.exit("Thanks for using my secret messages program")

                    mode = input("Are we going to encrypt/decrypt enter "\
                                 "'e' or 'd':")
                    if inWhileLoop:
                        str_from_user = input("What is the message?" + newline)

                    pad  = input("Please enter the pad number:")

                    onetimepad  = OneTimepad()
                    if mode == "encrypt" or mode == "e":
                        mode = "encrypt"
                        cipher = cipher_help.available_ciphers[cipher_from_user](keyword=keyword)
                        encrypted_message = cipher.encrypt(str_from_user)
                        messagepadded = onetimepad.encrypt(text=encrypted_message, mode=mode, pad=pad)
                        blocksfive = input("Encryption in blocks of 5? y/n:")
                        if blocksfive.upper() == "Y":
                            messagepadded_blocks = cipher_help.blocksoffive_encrypt(messagepadded)
                            print("encrypted message in blocks of 5: " + messagepadded_blocks)
                        else:
                            print("encrypted message: "+messagepadded)

                    elif mode == "decrypt" or mode == 'd':
                        blocksfive = input("Was encrpytion done in blocks of 5? y/n:")
                        if blocksfive.upper() == "Y":
                            str_from_user = cipher_help.blocksoffive_decrypt(str_from_user)
                        mode = "decrypt"
                        cipher = cipher_help.available_ciphers[cipher_from_user](keyword=keyword)
                        decrypted_message = onetimepad.decrypt(text=str_from_user, mode=mode, pad=pad)
                        messagepadded = cipher.decrypt(decrypted_message)
                        print("decrypted message: "+messagepadded+newline)
                    else:
                        print("Don't know that cipher. Let's try again."+newline)
                    inWhileLoop = True

if __name__ == "__main__":
    main()