# Substitution Cipher 

# CONSTANT Variables 
UPPER_ALPHABET = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

print(UPPER_ALPHABET)

# Variables 
# plaintext = "ILOVECAKE"
ciphertext = "" # Empty string 
shift = 13

plaintext = input("Enter plaintext: ").upper()
shift = int(input("Enter shift value: "))

for char in plaintext:
            ciphertext += UPPER_ALPHABET[((ord(char) - ord("A") + shift) % 26)]
    
print(plaintext)
print(ciphertext)
