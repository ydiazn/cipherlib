import unittest
from OneTimePadCipher import OneTimePadCipher

class OneTimePadCipherTest(unittest.TestCase):
    def test_encrypt_decrypt(self):
        cipher = OneTimePadCipher()
        message = "HELLO"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(message, decrypted)

if __name__ == '__main__':
    unittest.main()
