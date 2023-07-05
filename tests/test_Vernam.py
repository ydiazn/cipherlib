import unittest

# A funcção que nós vamos textar
def encriptar(messagem, chave):
    mensagem_encriptada = ""
    for i in range(len(messagem)):
        char = messagem[i]
        chave_char = chave[i % len(chave)]
        encriptada_char = chr(ord(char) ^ ord(chave_char))
        mensagem_encriptada += encriptada_char
    return mensagem_encriptada

def desencriptar(messagem, chave):
    mensagem_desencriptada = ""
    for i in range(len(messagem)):
        char = messagem[i]
        chave_char = chave[i % len(chave)]
        desencriptar_char = chr(ord(char) ^ ord(chave_char))
        mensagem_desencriptada += desencriptar_char
    return mensagem_desencriptada


# Exemplo
mensagem = "Eu amo estudar"
chave = "ola todos os di"


# # A classe de teste unitário
class TesteVernam(unittest.TestCase):

    def testeEncriptarMensagem(self):
        resultado1 = encriptar(mensagem, chave)
        resultado2 = desencriptar(resultado1, chave)

        self.assertEqual(resultado2,mensagem)

    

if __name__ == '__main__':
    unittest.main()