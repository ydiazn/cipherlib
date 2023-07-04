import unittest
import sys
import os

# Adicionar o diretório "ciphers" ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
ciphers_dir = os.path.join(current_dir, '..', 'ciphers')
sys.path.append(ciphers_dir)

# Importar o módulo AESCipher


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from AES import AESCipher


class AESCipherTests(unittest.TestCase):
    def test_encryption_decryption(self):
        key = get_random_bytes(16)
        cipher = AESCipher(key)

        plaintext = b'Mensagem secreta'
        ciphertext = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(ciphertext)

        self.assertEqual(decrypted_text, plaintext)


if __name__ == '__main__':
    unittest.main()
