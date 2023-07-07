# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
from utils import detectEnglish, pyperclip
message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # Run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # Get the number of the symbol
            num = num - key

            # Handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # Add the symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # Just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # Split the translated message into words
    words = translated.split()

    # Count the number of English words in the translated message
    english_word_count = sum(1 for word in words if detectEnglish.isEnglish(word))

    # If more than half of the words are English, print the message
    if english_word_count > len(words) / 2:
        print('Possible encryption hack:')
        print('Key %s: %s' % (key, translated[:100]))
        print()
        print('English word count:', english_word_count)
        print('Total word count:', len(words))
        break
