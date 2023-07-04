import decryption_methods

def decrypt_message(message):
    decryption_methods.decrypt_with_affine(message)
    print("-----------------------------------")
    decryption_methods.decrypt_with_transposition(message)

 