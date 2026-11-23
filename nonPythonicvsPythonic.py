

"""

Pythonic code vs non-Pythonic code

"""


# Looping 
arr = [1, 2, 3]

for i in range(len(arr)):
    print(arr[i])

for item in arr:
    print(item)


# Swapping values 
temp = 0; a = 3; b = 5

temp = a
a = b
b = temp

a, b = b, a


# List comprehensions 
numbers = [1, 2, 3]
squares = []
for n in numbers:
    squares.append(n * n)
    
squares = [n * n for n in numbers]
