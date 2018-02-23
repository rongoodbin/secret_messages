import helper_functions as help
import os
from onetimepad_cipher import OneTimepad

dash = "-"
available_ciphers_text = "These are the current available ciphers:\n"
newline = os.linesep

def showAvailableCiphers():
    print(available_ciphers_text)
    for cipher in help.available_ciphers:
        print(dash + cipher)


def main():
   welcome_text  = "This is the secret messages project for the Treehouse techdegree."+newline
   print(welcome_text)
   keyword = None

   while True:
      showAvailableCiphers()
      cipher_from_user = input("\nWhich cipher would you like to use?: ")
      if cipher_from_user in help.available_ciphers.keys():
         if cipher_from_user == "keyword":
             keyword = input("Keyword cipher is a fantastic cipher. Please enter a keyword to use?")
             str_from_user = input("What is the message?" + newline)

         else:
            str_from_user = input("That is a fantastic cipher. What is the message?"+newline)

         mode = input("Are we going to encrypt/decrypt enter 'e' or 'd':")

         pad  = input("Please enter the pad number:")
         onetimepad  = OneTimepad()

         if mode == "encrypt" or mode == "e":
             mode = "encrypt"
             cipher = help.available_ciphers[cipher_from_user](keyword=keyword)
             encrypted_message = cipher.encrypt(str_from_user)
             messagepadded = onetimepad.encrypt(text=encrypted_message, mode=mode, pad=pad)
             print("encrypted message: "+messagepadded)

         elif mode == "decrypt" or mode == 'd':
             mode = "decrypt"
             cipher = help.available_ciphers[cipher_from_user](keyword=keyword)
             decrypted_message = onetimepad.decrypt(text=str_from_user, mode=mode, pad=pad)
             messagepadded = cipher.decrypt(decrypted_message)


             print("decrypted message: "+messagepadded+newline)

      else:
            print("Don't know that cipher. Let's try again."+newline)



if __name__ == "__main__":
    main()