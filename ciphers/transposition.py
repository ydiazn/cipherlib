import math

class TranspositionCipher:

    def __init__(self, key):
        """Initialize instance.
        Args:
            key (str): secret key
        """
        self.key = key

    def encrypt(self, text):
        """Encrypt a clear text.
        Args:
            text (str): clear text
        Returns:
            str: encrypted text
        """
        ciphertext = [''] * self.key

        for col in range(self.key):
            pointer = col

            while pointer < len(text):

                ciphertext[col] += text[pointer]
                
                pointer += self.key

        return ''.join(ciphertext)


    def decrypt(self, text):
        """Decrypt an encrypted text.
        Args:
            text (str): clear text
        Returns:
            str: encrypted text
        """
        numOfColumns = math.ceil(len(text) / self.key)
        
        numOfRows = self.key

        numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)q

        plaintext = [''] * numOfColumns

        col = 0
        row = 0

        for symbol in text:
            plaintext[col] += symbol
            col += 1

            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):

                col = 0
                row += 1

        return ''.join(plaintext)
