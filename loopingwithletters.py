

"""

Looping with letters/strings 

"""




# No looping

# Concatenation 

temp = "a"

# "a" is 97 in ASCII. 
temp_ord = ord(temp)

# chr(97) returns "a".
print(temp, temp_ord, chr(temp_ord))

# "b" is 98 in ASCII.
temp = temp + "b"

temp_ord = temp_ord + 1

# chr(98) returns "b".
print(temp, temp_ord, chr(temp_ord))

# "c" is 99 in ASCII. 
temp = temp + "c"

temp_ord = temp_ord + 1

# chr(99) returns "c".
print(temp, temp_ord, chr(temp_ord))


print()
print()


# With looping

letters = ["a", "b", "c", "d", "e", "f"]

for letter in letters:
    print(letter)


print()
print()


letters = ["a", "b", "c", "d", "e", "f"]

temp = ""

for letter in letters:
    temp += letter
    print(temp)


print()
print()


temp = ""

for letter in range(5):
    temp = temp + "a"
    print(temp)
