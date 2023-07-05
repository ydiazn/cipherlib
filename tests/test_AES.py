import unittest
from Crypto.Random import get_random_bytes
from ciphers.AES import AESCipher


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
