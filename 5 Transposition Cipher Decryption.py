# Transposition Cipher Decryption
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import math, pyperclip

def main():
    message = input("Encrypted message: ")
    key = int(input("Enter Key: [1-10]: "))
    plainText = decryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(plainText + '|')
    pyperclip.copy(plainText)

def decryptMessage(key, message):
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0; row = 0;

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText)

if __name__ == "__main__":
    main()

