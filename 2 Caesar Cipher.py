# The Caesar Cipher
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip

message = input("Enter message: ")
key = int(input("Key [1-26]: "))
mode = input("Encrypt or Decrypt [e/d]: ")

if mode == "e" or mode == "E":
    mode = "encrypt"
elif mode == "d" or mode == "D":
    mode = "decrypt"

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

translated = ""

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

if mode == "encrypt":
    print("Encryption:", translated)
elif mode == "decrypt":
    print("Decryption:", translated)

pyperclip.copy(translated)
