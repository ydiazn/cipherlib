import unittest
from unittest import TestCase
"""import pyperclip, sys, random"""

from substituition import translateMessage, encryptMessage, decryptMessage

class SubstituitionTest(unittest.TestCase):

    def test_encriptMessage(self):
        encrypted = encryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Xavier Joao, Esta é uma informação para a familia Beatriz.')
        self.assertEqual(encrypted, 'Nejhws Tded, Wiue é gle hmbdsleçãd oese e belhahe Pweushz.')

    def test_decryptMessage(self):
        decrypted = decryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ','Nejhws Tded, Wiue é gle hmbdsleçãd oese e belhahe Pweushz.' )
        self.assertEqual(decrypted, 'Xavier Joao, Esta é uma informação para a familia Beatriz.')


    if __name__ == '__main__':
        unittest.main()
    
        

