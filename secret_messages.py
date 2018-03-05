import helper_functions as cipher_help
import os
from onetimepad_cipher import OneTimepad
import sys

dash = "-"
available_ciphers_text = "These are the current available ciphers:\n"
newline = os.linesep

def cls():
    print('\n'*50)


def welcome():
    welcome_text  = "This is the secret messages project for the Treehouse " \
                    "techdegree."+newline
    print(welcome_text)

"""
show the user all available ciphers
"""
def showAvailableCiphers():
    print(available_ciphers_text)
    for cipher in cipher_help.available_ciphers:
        print(dash + cipher)

def get_cipher_from_user():
    cipher_from_user = input("\nWhich cipher would you like to use?: ")
    if cipher_from_user in cipher_help.available_ciphers.keys():
        return cipher_from_user
    else:
        return None

    return cipher_from_user

def get_text_from_user(cipher_from_user, inWhileLoop):
    keyword = None
    if cipher_from_user == "keyword":
        if inWhileLoop:
            keyword = input("Please enter a keyword to use?")
        else:
            keyword = input("Keyword cipher is a fantastic cipher. Please enter a keyword to use?")

        str_from_user = input("What is the message?" + newline)

    else:
        if inWhileLoop:
            str_from_user = input("What is the message?" + newline)

        else:
            str_from_user = input("That is a fantastic cipher. What is the message?" + newline)

    return str_from_user,keyword


def get_mode_from_user(inWhileLoop):
    if inWhileLoop:
        answer = input("Would you like to encrypt/decrypt again? y/n:")
        if not answer.upper() == 'Y':
            sys.exit("Thanks for using secret message program. Bye now")

    mode = input("Are we going to encrypt/decrypt enter 'e' or 'd':")
    if mode == "encrypt" or mode == "e":
         mode = "encrypt"
    elif  mode == "decrypt" or mode == "d":
        mode = "decrypt"
    else:
        mode = None

    return mode

def get_one_time_pad_from_user():
    pad = input("Please enter the pad number:")
    if pad is None or pad == "":
        print("Need a value for the one time pad:")
        return None
    return pad

def encrypt_decrypt(cipher_from_user, str_from_user, keyword, mode, pad):
    onetimepad = OneTimepad()
    if mode == "encrypt" or mode == "e":
        mode = "encrypt"
        cipher = cipher_help.available_ciphers[cipher_from_user](
            keyword=keyword)
        encrypted_message = cipher.encrypt(str_from_user)
        messagepadded = onetimepad.encrypt(text=encrypted_message, mode=mode,
                                           pad=pad)
        blocksfive = input("Encryption in blocks of 5? y/n:")
        if blocksfive.upper() == "Y":
            messagepadded_blocks = cipher_help.blocksoffive_encrypt(
                messagepadded)
            print("encrypted message in blocks of 5: " + messagepadded_blocks)
        else:
            print("encrypted message: " + messagepadded)

    elif mode == "decrypt" or mode == 'd':
        blocksfive = input("Was encrpytion done in blocks of 5? y/n:")
        if blocksfive.upper() == "Y":
            str_from_user = cipher_help.blocksoffive_decrypt(str_from_user)
        mode = "decrypt"
        cipher = cipher_help.available_ciphers[cipher_from_user](
            keyword=keyword)
        decrypted_message = onetimepad.decrypt(text=str_from_user, mode=mode,
                                               pad=pad)
        messagepadded = cipher.decrypt(decrypted_message)
        print("decrypted message: " + messagepadded + newline)
    else:
        print("Don't know that cipher. Let's try again." + newline)

"""
Launch point is here in main()  - interact with the user. get the cipher they 
want to use and message to encrypt/decrypt.
Added in one time pad for extra security, in which case a number is requested 
from the user. Note, that with the one time pad. We perform the one time pad 
on encrypted text when encrypting and one time pad decryption is performed 
before decrypting using the selected cipher.
"""
def main():
    welcome()

    showAvailableCiphers()
    cipher_from_user = get_cipher_from_user()
    inWhileLoop = False
    while True:
       mode = get_mode_from_user(inWhileLoop)
       str_from_user, keyword = get_text_from_user(cipher_from_user,inWhileLoop)
       pad = get_one_time_pad_from_user()
       encrypt_decrypt(cipher_from_user,str_from_user, keyword, mode, pad)
       inWhileLoop = True


if __name__ == "__main__":
    main()


