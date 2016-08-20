# Vigenere Cipher Dictionary Hacker
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import detecting_english_programmatically as detectEnglish
import vigenere_cipher as vigCipher, pyperclip

def main():
    ciphertext = input('Encrypted message: ')
    hackedText = hackVigenere(ciphertext)

    if hackedText != None:
        print('Copying hacked message to clpboard:')
        print(hackedText)
        pyperclip.copy(hackedText)
    else:
        print('Failed to hack encryption.')

def hackVigenere(ciphertext):
    fo = open('Dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()
        decryptedText = vigCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage = 40):
            print('Possible encrypton break:')
            print('Key: ' + str(word) + ' | ' + decryptedText[:100])
            print('Enter D for done, or just pres Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
