# Simple Substituition Cipher

from .base import BaseCipher

class SimpleSubstitutionCipher(BaseCipher):
    def __init__(self, key):
        """Initialize instance.
        Args:
            key (str): secret key
        """
        self.key = key.upper()
        self.key_map = self.generate_key_map()

    def generate_key_map(self):
        """Generate a mapping for the key."""
        key_map = {}
        for i, letter in enumerate(self.key):
            key_map[letter] = chr(ord('A') + i)
        return key_map

    def transform(self, text, encrypt=True):
        text = text.upper()
        transformed = ''

        for symbol in text:
            if symbol.isalpha():
                if encrypt:
                    transformed += self.key_map.get(symbol, symbol)
                else:
                    transformed += list(self.key_map.keys())[list(self.key_map.values()).index(symbol)]
            else:
                transformed += symbol

        return transformed

    def encrypt(self, text):
        return self.transform(text, encrypt=True)

    def decrypt(self, text):
        return self.transform(text, encrypt=False)
