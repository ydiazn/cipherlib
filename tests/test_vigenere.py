import unittest
from unittest import TestCase
#from ciphers.vigenere import VigenereCipher

from ciphers.vigenereCipher import encryptMessage, decryptMessage
class VigenereTest(unittest.TestCase):

    def test_encrypt(self):
        encrypted = encryptMessage('ABAD', 'Alan Mathison Turing was a British mathematician The message has been copied to the clipboard.')
        self.assertEqual(encrypted, 'Amaq Mbtkitoq Tvrlnh wds b Buiuivh nawhfmdtjclao Tke nevsbgh hbs eefn foqihd uo whf coiqbrasd.')
        
    def test_decrypt(self):
        decrypted = decryptMessage('ABAD', 'Amaq Mbtkitoq Tvrlnh wds b Buiuivh nawhfmdtjclao Tke nevsbgh hbs eefn foqihd uo whf coiqbrasd.')
        self.assertEqual(decrypted, 'Alan Mathison Turing was a British mathematician The message has been copied to the clipboard')
  
if __name__ == '__main__':
    unittest.main()