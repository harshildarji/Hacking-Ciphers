# Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip
transDecrypt = __import__('5 Transposition Cipher Decryption')
detectEnglish = __import__('8 Detecting English Programmatically')

def main():
    message = input('Enter encrypted message: \n')
    hackedMessage = hackTransposition(message)

    if hackedMessage == None:
        print('Failed to hack encryption')
    else:
        print('Hacked message is copied clipboard.')
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('[press Ctrl+C or Ctrl+D to quit at any time]')

    for key in range(1, len(message)):
        print('Trying key #%s...' % key)
        decryptedText = transDecrypt.decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptedText, 50):
            print('\nPossible encryption hack:')
            print('Key #%s: %s' % (key, decryptedText[:100]))
            print("\nEnter 'D' for done or just press 'Enter' to continue hacking:")
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
