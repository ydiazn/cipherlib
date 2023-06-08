import unittest
from unittest import TestCase

from ciphers.affine import affineCipher


class affineTest(TestCase):
    def test_encrypt(self):
        cipher = affineCipher(key=1)
        encrypted = cipher.encryptMessaget('Clear text')

        self.assertEqual(encrypted, 'DMFBS UFYU')

    def test_decrypt(self):
        cipher = affineCipher(key=1)
        clear = cipher.decryptMessage('Dmfbs ufyu')

        self.assertEqual(clear, 'CLEAR TEXT')



if __name__ == '__main__':
    unittest.main()