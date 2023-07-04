from .base import BaseCipher


class PlayFairCipher(BaseCipher):
    def generate_playfair_matrix(self, key):
        key = key.replace(" ", "").upper()
        key = key.replace("J", "I")  # Substitui 'J' por 'I'
        key = "".join(dict.fromkeys(key))  # Remove caracteres duplicados
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
       
        # Preenche a matriz com as letras do alfabeto
        for char in key:
            alphabet = alphabet.replace(char, "")

        matrix = list(key + alphabet)


        # Agrupa os caracteres em uma matriz 5x5
        playfair_matrix = []
        for i in range(5):
            row = matrix[i * 5 : (i + 1) * 5]
            playfair_matrix.append(row)

        return playfair_matrix

    def get_position(self, matrix, char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None, None


    def transform(self, text, key):
        matrix = self.generate_playfair_matrix(key)
        print(matrix)
        transformed = ""

        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) < 2:
                pair += 'X'

            row1, col1 = self.get_position(matrix, pair[0])
            row2, col2 = self.get_position(matrix, pair[1])

            if row1 == row2:
                transformed += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                transformed += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                transformed += matrix[row1][col2] + matrix[row2][col1]

        return transformed



    def encrypt(self, text):
        transformed = self.transform(text, self.key)
        return transformed

    def decrypt(self, text):
        transformed = self.transform(text, self.key)
        return transformed



