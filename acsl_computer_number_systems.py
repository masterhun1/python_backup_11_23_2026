
# Decimal, binary, octal, & hex

decimal = 55
# decimal = 255
# decimal = 100
# decimal = 240
# decimal = 15


binary = bin(decimal)
binary = binary[2:]

if decimal < 2:
    binary = "0000000" + binary
elif decimal < 4:
    binary = "000000" + binary
elif decimal < 8:
    binary = "00000 " + binary
elif decimal < 16:
    binary = "0000 " + binary
elif decimal < 32:
    binary = "000" + binary
elif decimal < 64:
    binary = "00" + binary
elif decimal < 128:
    binary = "0" + binary

binary = binary[:4] + " " + binary[4:]

octal = oct(decimal)
octal = octal[2:]
hex_value = hex(decimal)
hex_value = hex_value[2:]

# Debugging 
# print(decimal, binary, octal, hex)

output = f"Decimal: {decimal}   Binary: {binary}   Octal: {octal}   Hex: {hex_value}"

print(output)


print(); print()

# Python code 
# Year in decimal to octal, octal digits in ascending order, then octal to hex.
year = 2019 
# year = 2026 

# Debugging 
# print(oct(year))

octal = str(oct(year))
octal = octal[2:]

# Debugging 
# print(octal)

print(f"The year in decimal is ... {year}")
print(f"The year {year} in decimal is {octal} in octal.")

octal_digits = list(octal)

# Debugging 
# print(octal_digits)

octal_digits.sort()

# Debugging 
# print(octal_digits)
new_octal = "".join(octal_digits)
# print(new_octal)
print(f"The digits in {octal} in ascending order is {new_octal}.")
# print(int(new_octal, 8))
new_hex = hex(int(new_octal, 8))

# Debugging 
# print(new_hex)

new_hex = new_hex[2:].upper()
print(f"The octal number {new_octal} converted to hex is {new_hex}.")












