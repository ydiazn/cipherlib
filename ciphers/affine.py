# Affine Cipher

import sys
import random


from ciphers.base import BaseCipher
from utils import cryptomath, pyperclip


class AffineCipher(BaseCipher):
    SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""  # note the space at the front

    def __init__(self):
        self.myMessage = """"f-T))h<RhH)?"""
        self.myKey = 2023
        self.myMode = 'decrypt'  # set to 'encrypt' or 'decrypt'

    def main(self):
        if self.myMode == 'encrypt':
            translated = self.encryptMessage(self.myKey, self.myMessage)
        elif self.myMode == 'decrypt':
            translated = self.decryptMessage(self.myKey, self.myMessage)
        print('Key: %s' % (self.myKey))
        print('%sed text:' % (self.myMode.title()))
        print(translated)
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (self.myMode))

    def getKeyParts(self, key):
        keyA = key // len(self.SYMBOLS)
        keyB = key % len(self.SYMBOLS)
        return keyA, keyB

    def checkKeys(self, keyA, keyB, mode):
        if keyA == 1 and mode == 'encrypt':
            sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
        if keyB == 0 and mode == 'encrypt':
            sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
        if keyA < 0 or keyB < 0 or keyB > len(self.SYMBOLS) - 1:
            sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(self.SYMBOLS) - 1))
        if cryptomath.gcd(keyA, len(self.SYMBOLS)) != 1:
            sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (
            keyA, len(self.SYMBOLS)))

    def encryptMessage(self, key, message):
        keyA, keyB = self.getKeyParts(key)
        self.checkKeys(keyA, keyB, 'encrypt')
        ciphertext = ''
        for symbol in message:
            if symbol in self.SYMBOLS:
                # encrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                ciphertext += self.SYMBOLS[(symIndex * keyA + keyB) % len(self.SYMBOLS)]
            else:
                ciphertext += symbol  # just append this symbol unencrypted
        return ciphertext

    def decryptMessage(self, key, message):
        keyA, keyB = self.getKeyParts(key)
        self.checkKeys(keyA, keyB, 'decrypt')
        plaintext = ''
        modInverseOfKeyA = cryptomath.findModInverse(keyA, len(self.SYMBOLS))

        for symbol in message:
            if symbol in self.SYMBOLS:
                # decrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                plaintext += self.SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(self.SYMBOLS)]
            else:
                plaintext += symbol  # just append this symbol undecrypted
        return plaintext

    def getRandomKey(self):
        while True:
            keyA = random.randint(2, len(self.SYMBOLS))
            keyB = random.randint(2, len(self.SYMBOLS))
            if cryptomath.gcd(keyA, len(self.SYMBOLS)) == 1:
                return keyA * len(self.SYMBOLS) + keyB


# If affine.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    cipher = AffineCipher()
    cipher.main()
