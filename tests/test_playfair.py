import unittest
from ciphers.playfair_cipher import PlayFairCipher

class PlayFairCipherTest(unittest.TestCase):
    def test_encrypt(self):
        cipher = PlayFairCipher(key="CIFRA")
        encrypted = cipher.encrypt("CARRO")
        self.assertEqual(encrypted, "ICAAMZ")

    '''def test_decrypt(self):
        cipher = PlayFairCipher(key="CIFRA")
        clear = cipher.decrypt("BGMMLZNAQL")
        self.assertEqual(clear, "HELLOWORLD")'''


if __name__ == '__main__':
    unittest.main()
