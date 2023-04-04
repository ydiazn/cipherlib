import unittest
from unittest import TestCase

from ciphers.cesar import CesarCipher


class CesarTest(TestCase):
    def test_encrypt(self):
        cipher = CesarCipher(key=1)
        encrypted = cipher.encrypt('Clear text')

        self.assertEqual(encrypted, 'DMFBS UFYU')

    def test_decrypt(self):
        cipher = CesarCipher(key=1)
        clear = cipher.decrypt('Dmfbs ufyu')

        self.assertEqual(clear, 'CLEAR TEXT')



if __name__ == '__main__':
    unittest.main()