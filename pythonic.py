

# FYI: Ask ChatGPT. Do you agree with ChatGPT? Or do you disagree? If so, why?

# a. What is the difference?

arr = [1, 2, 3]

for i in range(len(arr)):
    print(arr[i])

# vs.

for item in arr:
    print(item)

print(); print()


#b. What is the difference?

temp = 0; a = 3; b = 5

print(temp, a, b)

temp = a
a = b
b = temp

print(temp, a, b)

# vs.

print(temp, a, b)

a, b = b, a

print(temp, a, b)


print(); print()

# c. What is the difference?

numbers = [1, 2, 3, 4]

squares = []

for n in numbers:
    squares.append(n * n)

# vs.

squares = [n * n for n in numbers]



# *** THE END ***


