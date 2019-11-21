import math as m
from random import randint

def Encrypt_Cezar(text = "abc", key = 777):
    ''' Encrypt_Cezar is a function takes 1 argument string, and returns text encrypted in Cezar cipher. If no argument passed, default argument  = "abc" Rot 1'''

    encrypted_str = text
    if key == 777:
        # for testing max shift  = 9
        key = randint(1,9)

    result = ""

    # traverse text
    for i in range(len(encrypted_str)):
        char = encrypted_str[i]

        # Shift (uppercase characters)
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Shift (lowercase characters)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result, key


def Decrypt_Cezar(key, message):
    ''' function decrypts cezar cypher  req. @param (key, msg) 
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter + " "

    return result

# ---- test test test ---------
if __name__ == "__main__":
    enc, key= Encrypt_Cezar("a df  d")
    print(enc + str(key))

    dec = Decrypt_Cezar(key, enc)
    print(dec)

else:
    pass
