from hacking import transpositionHacker, affineHacker, vigenereHacker

def decrypt_with_transposition(message):
    print("Decifrando usando a Cifra de Transposição...")
    decrypted_message = transpositionHacker.hackTransposition(message)
    if decrypted_message is not None:
        print("Mensagem decifrada usando a Cifra de Transposição:")
        print(decrypted_message)
    else:
        print("Falha ao decifrar a mensagem usando a Cifra de Transposição.")

def decrypt_with_affine(message):
    print("Decifrando usando a Cifra de Afine...")
    decrypted_message = affineHacker.hackAffine(message)
    if decrypted_message is not None:
        print("Mensagem decifrada usando a Cifra de Afine:")
        print(decrypted_message)
    else:
        print("Falha ao decifrar a mensagem usando a Cifra de Afine.")


def decrypt_with_vigenere(message):
    print("Decifrando usando a Cifra de Afine...")
    decrypted_message = vigenereHacker.hackVigenere(message)
    if decrypted_message is not None:
        print("Mensagem decifrada usando a Cifra de Vigenere:")
        print(decrypted_message)
    else:
        print("Falha ao decifrar a mensagem usando a Cifra de Vigenere.")

def decrypt_message(message):
    decrypt_with_transposition(message)
    print("-----------------------------------")
    decrypt_with_affine(message)
    print("-----------------------------------")
    decrypt_with_vigenere(message)
