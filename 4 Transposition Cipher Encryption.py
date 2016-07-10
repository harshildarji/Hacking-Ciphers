# Transposition Cipher Encryption
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip

def main():
    message = input('Enter message: ')
    key = int(input('Enter key [1-10]: '))
    cipherText = encryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(cipherText + '|')
    pyperclip.copy(cipherText)

def encryptMessage(key, message):
    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

if __name__ == '__main__':
    main()
    


