
"""

The FizzBuzz Problem Solved Using Procedural Programming 

Source: Mr. Hun 

"""


# Constant variables 
MAX = 25
FIZZ = 3
BUZZ = 5
FIZZBUZZ = FIZZ * BUZZ 


# Variables 
# N/A

# Procedure 
def fizzbuzz(num):
    result = str(num)
    if num % FIZZ == 0 and num % BUZZ == 0:
        result = "FIZZBUZZ"
    elif num % FIZZ == 0:
        result = "FIZZ"
    elif num % BUZZ == 0:
        result = "BUZZ"
    return result



# Example output

# Output displayed from top down
for num in range(1, MAX + 1):
    print(fizzbuzz(num))
