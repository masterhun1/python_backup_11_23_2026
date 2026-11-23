

# enumerate


for i, char in enumerate(list(range(100))):
    print(i, char)


for i, char in enumerate(list(range(100))):
    # What is at the index of the value 50 in the list?
    if char == 50:
        print(i, char)


for i, char in enumerate(list(range(10))):
    # What is at the 50th position?
    print(i, char)
    if  char == 5:
        print(i, char)

