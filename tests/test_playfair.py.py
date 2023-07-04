import unittest
from PlayFairCipher import PlayFairCipher

class PlayFairCipherTest(unittest.TestCase):
    def test_encrypt(self):
        cipher = PlayFairCipher(key="CIFRA")
        encrypted = cipher.encrypt("KCQAMPRLCOAR")
        self.assertEqual(encrypted, "HELLOWORLD")

    '''def test_decrypt(self):
        cipher = PlayFairCipher(key="CIFRA")
        clear = cipher.decrypt("KCQAMPRLCOAR")
        self.assertEqual(clear, "HELLOWORLD")'''


if __name__ == '__main__':
    unittest.main()
