
"""

The FizzBuzz Problem Solved Using Functional Programming 

Source: Google AI 

"""

# A pure function mapping an input to its FizzBuzz representation
fizzbuzz_logic = lambda x: (
    "FizzBuzz" if x % 15 == 0 else
    "Fizz" if x % 3 == 0 else
    "Buzz" if x % 5 == 0 else
    str(x)
)

# Higher-order function processing the iterable sequence
def run_fizzbuzz(limit: int) -> list:
    return list(map(fizzbuzz_logic, range(1, limit + 1)))

# Example output
print(run_fizzbuzz(15))

output = run_fizzbuzz(15)

print()

# Output displayed from top down
for item in output:
    print(item)
