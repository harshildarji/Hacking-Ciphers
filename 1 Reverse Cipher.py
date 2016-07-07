# The Reverse Cipher
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

# The reverse cipher is a very weak cipher, but as a beginner this is a very
# easy to understand cipher.

message = input("Enter message: ")
translated = ""

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i -= 1

print(translated)
