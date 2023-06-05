from .base import BaseCipher

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class VigenereCipher(BaseCipher):
    def translateMessage(key, message, mode):
        translated = [] # stores the encrypted/decrypted message string

        keyIndex = 0
        key = key.upper()

        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex]) # add if encrypting
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

                num %= len(LETTERS) # handle the potential wrap-around

                # add the encrypted/decrypted symbol to the end of translated.
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # The symbol was not in LETTERS, so add it to translated as is.
                translated.append(symbol)

        return ''.join(translated)

    
    def encrypt(key, text):

        return translateMessage(key, text, 'encrypt')


    def decrypt(key, text):

        return translateMessage(key, text, 'decrypt')

    
