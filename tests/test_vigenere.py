import unittest
from unittest import TestCase
from ciphers.vigenere import VigenereCipher


class VigenereTest(unittest.TestCase):

    def test_encrypt(self):
        encrypted = cipher.encrypt('verdade', 'o florindo e inteligente')
        self.assertEqual(encrypted, 'j jcrrlrys v lnwigmxhnwi')
        
    def test_decrypt(self):
        decrypted = cipher.decrypt('verdade', 'j jcrrlrys v lnwigmxhnwi')
        self.assertEqual(decrypted, 'o florindo e inteligente')
  
if __name__ == '__main__':
    unittest.main()