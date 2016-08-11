# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('Enter message: ')
    key = input('Enter key [alphanumeric]: ')
    mode = input('Encrypt/Decrypt [e/d]: ')

    if mode.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)

    pyperclip.copy(translated)
    print('\n%sed message has been copied to clipboard:' % mode.title())
    print(translated)

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

if __name__ == '__main__':
    main()
