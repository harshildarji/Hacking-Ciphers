# RSA Key Generator
# Source: http://inventwithpython.com/hacking (BSD Licensed)

import random, sys, os
import rabin_miller as rabinMiller, cryptomath_module as cryptoMath

def main():
    print('Making key files...')
    makeKeyFiles('rsa', 1024)
    print('\nKey files generation successful.')

def generateKey(keySize):
    print('Generating prime p...')
    p = rabinMiller.generateLargePrime(keySize)
    print('Generating prime q...')
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    print('Generating e that is relatively prime to (p - 1) * (q - 1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print('Calculating d that is mod inverse of e...')
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('\nPublic key:', publicKey)
    print('\nPrivate key:', privateKey)

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        print('\nWARNING:')
        print('"%s_pubkey.txt" or "%s_privkey.txt" already exists. \nUse a different name or delete these files and re-run this program.' % (name, name))
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print('\nPublic key is %s and %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % name)
    with open('%s_pubkey.txt' % name, 'w') as fo:
        fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))

    print('\nPrivate key is %s and %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing public key to file %s_privkey.txt...' % name)
    with open('%s_privkey.txt' % name, 'w') as fo:
        fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))

if __name__ == '__main__':
    main()
