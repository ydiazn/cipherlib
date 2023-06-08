

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    myMessage = """Hdello worl"""\

    hackedMessage = hackTransposition(myMessage)

#Nesta parte, verificamos se a mensagem hackeada é nula. Se for nula, exibimos a mensagem de falha na tentativa de hackear a criptografia. Caso contrário, exibimos a mensagem hackeada na tela e copiamos para a área de transferência usando o módulo pyperclip.
    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    
def hackTransposition(message):
    print('Hacking...')
#Exibe uma mensagem informando que as teclas Ctrl-C ou Ctrl-D podem ser pressionadas para sair a qualquer momento.
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

#Inicia um loop que itera através de uma série de possíveis chaves de descriptografia. A faixa é de 1 a len(message), ou seja, do tamanho mínimo da chave possível até o tamanho da mensagem.
    for key in range(1, len(message)):
#Exibe a chave atual que está sendo testada.
        print('Trying key #%s...' % (key))

#Chama a função decryptMessage do módulo transpositionDecrypt para descriptografar a mensagem usando a chave atual. O resultado é armazenado na variável decryptedText.
        decryptedText = transpositionDecrypt.decryptMessage(key, message)
#Verifica se o texto descriptografado é considerado como inglês com a ajuda da função isEnglish do módulo detectEnglish.
        if detectEnglish.isEnglish(decryptedText):

#Se o texto descriptografado for considerado como inglês, exibe uma mensagem indicando que uma possível descriptografia foi encontrada. Em seguida, exibe a chave e uma parte do texto descriptografado.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()

#Solicita ao usuário uma entrada para decidir se deseja parar o processo de hacking ou continuar tentando.
            print('Enter D for done, or just press Enter to continue hacking:')

            response = input('> ')
#Se a entrada do usuário começar com 'D' (ignorando espaços em branco e tornando-a maiúscula), a função retorna o texto descriptografado.
            if response.strip().upper().startswith('D'):
                return decryptedText
#Caso contrário, a função continua o loop com a próxima chave.
    return None

if __name__ == '__main__':
    main()




