from .base import BaseCipher

class OneTimePadCipher(BaseCipher):
    def __init__(self):
        self.key = self.generate_key(10)

    def generate_key(self, message_length):
        """Gera uma chave aleatória do mesmo tamanho da mensagem"""
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = [random.choice(letters) for _ in range(message_length)]
        return key

    def transform(self, text, key):
        text = text.upper()
        transformed = ''

        for i, symbol in enumerate(text):
            if symbol.isalpha():
                index = ord(symbol) - ord('A')
                key_index = ord(key[i % len(key)]) - ord('A')

                new_index = (index + key_index) % 26
                encrypted_symbol = chr(new_index + ord('A'))
                transformed += encrypted_symbol

        return transformed

    def encrypt(self, text):
        return self.transform(text, self.key)

    def decrypt(self, text):
        return self.transform(text, self.key)
