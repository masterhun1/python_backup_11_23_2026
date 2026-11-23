


table =  [ [25, 5, 5], 
           [50, 2, 25], 
           [7, 8, 9]  ]

num1 = table[0:0]
print(num1)
num2 = table[0:1]
op = "/"
math_question = f"{num1} {op} {num2}?"
print(math_question)
ans = table[0:2]
user_ans = int(input("Enter your answer as an integer: "))
if ans == user_ans:
    print("Correct!")
else:
    print("Incorrect!")



"""
import random 
num1 = random.randint(5, 10)
num2 = random.randint(5, 10)
print(divmod(num1, num2))
div_remainder = divmod(num1, num2)[1]
if div_remainder == 0:
    print(num1, num2)
    print("No remainder to worry about.")
else:
    print(num1, num2)
    print("There is a remainder.")
"""
