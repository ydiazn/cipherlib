from .base import BaseCipher


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class CesarCipher(BaseCipher):
    def transform(self, text, key):
        text = text.upper()
        transformed = ''

        for symbol in text:
            index = LETTERS.find(symbol)

            if index == -1:
                encrypt_symbol = symbol
            else:
                new_index = (index + key) % len(LETTERS)
                encrypt_symbol = LETTERS[new_index]

            transformed += encrypt_symbol

        return transformed

    def encrypt(self, text):
        return self.transform(text, self.key)

    def decrypt(self, text):
        return self.transform(text, -self.key)
