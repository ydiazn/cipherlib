import unittest
from unittest import TestCase

from ciphers.transposition import TranspositionCipher


class TranspositionTest(TestCase):
    def test_encrypt(self):
        cipher = TranspositionCipher(key=8)
        encrypted = cipher.encrypt('Common sense is not so common.')

        self.assertEqual(encrypted, 'Cenoonommstmme oo snnio. s s c')

    def test_decrypt(self):
        cipher = TranspositionCipher(key=8)
        clear = cipher.decrypt('Cenoonommstmme oo snnio. s s c')

        self.assertEqual(clear, 'Common sense is not so common.')



if __name__ == '__main__':
    unittest.main()