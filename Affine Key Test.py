# Affine Key Test
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

# This program proves that the keyspace of the affine cipher is limited to len(SYMBOLS) ^ 2.

cryptoMath = __import__('Cryptomath Module')
affineCipher = __import__('Affine Cipher')

message = 'Make things as simple as possible, but not simpler.'
print('Message: %s\nEncryption using key,' % message)
for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print('%s | %s' % (keyA, affineCipher.encryptMessage(key, message)))
