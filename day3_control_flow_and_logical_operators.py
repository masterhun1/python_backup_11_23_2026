

"""

Day 3: Control Flow and Logical Operators 

"""

"""
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

total = 0 

print("Welcome to Python Pizza Deliveries!")

# size choice?

size = input("What size pizza do you want? S, M, r L: ")

if size == "s" or size == "S":
    total += 15
elif size == "m" or size == "M":
    total += 20
elif size == "l" or size == "L":
    total += 25
else:
    print("Input error. Try again.")

# pepperoni?

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == "y" or pepperoni == "Y":
    if size == "s" or size == "S":
        total += 2
    else:
        total += 3

# extra cheese?

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "y" or extra_cheese == "Y":
    total += 1


# Output
print(f"Your final bill is : ${total}.")


# THE END 
