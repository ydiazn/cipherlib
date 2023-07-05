from decryptor.decryption_methods import decrypt_message
if __name__ == "__main__":
    print("Bem-vindo ao decifrador de mensagens!")
    encrypted_message = input("Insira a mensagem criptografada: ")
    decrypt_message(encrypted_message)
