

# Check for pyperclip compatibility. 
try:
  import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
  pass  # If pyperclip is not installed, do nothing. It's no big deal.



# Constants

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LOWER_ALPHABET = "abcdefghijlkmnopqrstuvwxyz"


char = "A"

# ord() function 
char_int = ord("A")

# Escape character 
print("\n")

print(char)

print("\n")

print(char_int)

print("\n")

# Empty string 
temp_string = ""

print("\n\n")

# Verifying for UPPER_ALPHABET
for char in range(26):
  temp_string += chr(char + char_int)

print(temp_string)

print(UPPER_ALPHABET == temp_string)
# Output: True 


# Encryption with a simple substitution cipher 

shift = -1

# plaintext = "PYTHONISAWESOME"
plaintext = "THERECANBEONLYONE"
# plaintext = "THEEAGLEHASLANDED"
# plaintext = "ATTACKATDAWN"
# plaintext = "DRINKMOREOLVATINE"
# plaintext = "LUKEIAMYOURFATHER"
# plaintext = "THEBUTLERDIDIT"
# plaintext = "DIDIDOTHAT"
# plaintext = "MYBADDOG"
# plaintext = "EATMOREVEGGIES"

ciphertext = ""

for char in plaintext:
  ciphertext += UPPER_ALPHABET[((ord(char) - ord("A") + shift) % 26)]

print()
print(plaintext)
print(ciphertext)


# Decryption 

# shift = ? 

message = ""

for char in ciphertext:
  message += UPPER_ALPHABET[((ord(char) - ord("A") - shift) % 26)]

print(message)



try:
  # Copy the translation to the clipboard:
  pyperclip.copy(message)
  print('(Copied to clipboard.)')
except:
  pass









