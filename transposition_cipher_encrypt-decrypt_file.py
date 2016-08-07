# Transposition Cipher Encrypt/Decrypt File
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import time, os, sys, transposition_cipher_encryption as transEncrypt
import transposition_cipher_decryption as transDecrypt

def main():
    inputFile = 'Frankenstein.txt'
    outputFile = 'Output.txt'
    key = int(input('Enter key [1-25]: '))
    mode = input('Encrypt/Decrypt [e/d]: ')

    if not os.path.exists(inputFile):
        print('File %s does not exist. Quitting...' % inputFile)
        sys.exit()
    if os.path.exists(outputFile):
        print('Overwrite %s? [y/n]' % outputFile)
        response = input('> ')
        if not response.lower().startswith('y'):
            sys.exit()
            
    startTime = time.time()
    if mode.lower().startswith('e'):
        content = open(inputFile).read()
        translated = transEncrypt.encryptMessage(key, content)
    elif mode.lower().startswith('d'):
        content = open(outputFile).read()
        translated = transDecrypt.decryptMessage(key, content)

    outputObj = open(outputFile, 'w')
    outputObj.write(translated)
    outputObj.close()
    
    totalTime = round(time.time() - startTime, 2)
    print('Done (', totalTime, 'seconds )')
    
if __name__ == '__main__':
    main()
