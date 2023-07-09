import unittest
from ciphers.substituition import SimpleSubstitutionCipher


class SimpleSubstitutionTest(unittest.TestCase):
    def test_encrypt(self):
        cipher = SimpleSubstitutionCipher(key='ZYXWVUTSRQPONMLKJIHGFEDCBA')
        encrypted = cipher.encrypt(' XAVIER JOAO, ESTA É UMA INFORMAÇÃO PARA A FAMILIA BEATRIZ.')

        self.assertEqual(encrypted, 'NEJHWS TDED, WIUE É GLE HMBDSLEÇÃD OESE E BELHAHE PWEUSHZ.')

    def test_decrypt(self):
        cipher = SimpleSubstitutionCipher(key='ZYXWVUTSRQPONMLKJIHGFEDCBA')
        decrypted = cipher.decrypt('NEJHWS TDED, WIUE É GLE HMBDSLEÇÃD OESE E BELHAHE PWEUSHZ.')

        self.assertEqual(decrypted,  'XAVIER JOAO, ESTA É UMA INFORMAÇÃO PARA A FAMILIA BEATRIZ.')


if __name__ == '__main__':
    unittest.main()

    

