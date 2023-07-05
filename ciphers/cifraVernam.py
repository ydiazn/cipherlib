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
chave = "ola na vida "

encriptada = encriptar(mensagem, chave)
desencriptada = desencriptar(encriptada, chave)

print("Mensagem encriptada:",encriptada)
print("Mensagem desencriptada:",desencriptada)





