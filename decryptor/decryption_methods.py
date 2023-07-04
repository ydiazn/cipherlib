from hacking import transpositionHacker, affineHacker


def decrypt_with_affine(message):
    print("Decifrando usando a Cifra de Afine...")
    decrypted_message = affineHacker.hackAffine(message)
    if decrypted_message is not None:
        print("Mensagem decifrada usando a Cifra de Afine:")
        print(decrypted_message)
    else:
        print("Falha ao decifrar a mensagem usando a Cifra de Afine.")

def decrypt_with_transposition(message):
    print("Decifrando usando a Cifra de Transposição...")
    decrypted_message = transpositionHacker.hackTransposition(message)
    if decrypted_message is not None:
        print("Mensagem decifrada usando a Cifra de Transposição:")
        print(decrypted_message)
    else:
        print("Falha ao decifrar a mensagem usando a Cifra de Transposição.")
