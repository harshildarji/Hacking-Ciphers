# Transposition Cipher Test
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import random, sys, transposition_cipher_encryption as transEncrypt
import transposition_cipher_decryption as transDecrypt

def main():
    random.seed(42)
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #%s: "%s..."' % (i + 1, message[:50]))
        for key in range(1, len(message)):
            encrypted = transEncrypt.encryptMessage(key, message)
            decrypted = transDecrypt.decryptMessage(key, encrypted)
            if message != decrypted:
                print('\nMismatch with key: %s & Message: %s' % (key, message))
                print('\nEncrypted:', encrypted)
                print('\nDecrypted:', decrypted)
                sys.exit()
    print('Transposition Cipher Test Passed')

if __name__ == '__main__':
    main()
