hex_digits = [hex(count)[2:].upper() for count in range(1, 16)]
print(hex_digits)

multiples_of_16 = [int(hex_digit,16) * 16 for hex_digit in hex_digits]
print(multiples_of_16)

index = 0
while True:
    if index > 14:
        index = 0
    print(f"What is {hex_digits[index]} * 16 = ?")
    ans = input()
    if int(ans) == multiples_of_16[index]:
        print("Correct!")
    else:
        print("Incorrect!")
    char = input("To quit, press x or X. Hit <ENTER> to continue.")
    if char in ["x", "X"]:
        break
    else:
        if index <= 14:
            index += 1

