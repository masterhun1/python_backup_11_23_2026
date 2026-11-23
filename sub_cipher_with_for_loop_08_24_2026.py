# Filename: sub_cipher_with_for_loop_08_24_2026.py


# shift = 1
shift = int(input("Enter shift value: "))

ciphertext = ""

# plaintext = "abc"
plaintext = input("Enter plaintext: ")

A_ASCII_Code = ord("A")

# Make sure plaintext has only uppercase letters.
plaintext = plaintext.upper() # Step 0 

for letter in plaintext:
    letter_ASCII_Code = ord(letter) # Step 1: Get ASCII code.
    #print(letter, letter_ASCII_Code)
    letter_position = letter_ASCII_Code - A_ASCII_Code # Step 2: Subtract 65. 
    new_letter_position = letter_position + shift # Step 3: Add shift. 
    new_letter_position = new_letter_position % 26 # Step 4: MOD by 26.
    #print(new_letter_position)
    new_letter_ASCII = new_letter_position + A_ASCII_Code # Step 5: Add back 65.
    #print(new_letter_ASCII)
    secret_letter = chr(new_letter_ASCII) # Step 6: ASCII code to letter. 
    ciphertext += secret_letter # Step 7: Concatenate cipher letter to ciphertext.
    
print(ciphertext)
