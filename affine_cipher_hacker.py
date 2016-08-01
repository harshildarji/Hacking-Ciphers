# Affine Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip, affine_cipher as affineCipher
import detecting_english_programmatically as detectEnglish
import cryptomath_module as cryptoMath

SILENT_MODE = False

def main():
    message = input('Encrypted message: ')
    hackedMessage = hackAffine(message)

    if hackedMessage != None:
        print('Copying hacked message to clipboard...')
        print('\nHacked message:\n', hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encrypton.')

def hackAffine(message):
    print('Hacking...\n[Press CTRL + C or CTRL + D to quit at any time]')
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Key #%s: %s...' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            print('\nPossible encryption hack:')
            print('Key #%s: %s...' % (key, decryptedText[:40]))
            print("Enter 'D' for done, or just press 'Enter' to continue hacking:")
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
