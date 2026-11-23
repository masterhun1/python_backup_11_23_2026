# 
# 
# Python Typing Text Effect
# 
# Source: 101 Computing [dot] net
# www.101computing.net/python-typing-text-effect/
# 
# 


import time, os, sys


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")


# The start sequence
typingPrint("Greetings, ready to take a Python quiz today? \n")
time.sleep(1)
typingPrint("I have three Python questions for you. \n")
time.sleep(1)

# Wipes the console/screen/output area.
time.sleep(1)  
clearScreen()

# Question #1 
# Added an escape character (\n) to break up the following string into 2 lines.
answer = typingInput("Question #1\nWhat is the output of this code? \nprint(1 % 0) \nType your answer using correct lowercase & uppercase: ")

if answer == "ZeroDivisionError" or answer == "zerodivisionerror":
  typingPrint("You answered " + answer + ". \n")
  typingPrint("You are correct!\n")
  typingPrint("The output of this code is ZeroDivisionError. \n")
elif answer != "ZeroDivisionError":
  typingPrint("You answered incorrectly. \n")
  typingPrint(answer + " is not ZeroDivisionError. \n")
  typingPrint("Please, review Python exceptions. \n")
else:
  typingPrint("Invalid input \n")


# Wipes the console/screen/output area.
time.sleep(1)  
clearScreen()


# Question #2 
# Added an escape character (\n) to break up the following string into 2 lines.
answer = typingInput("Question #2\nWhat is the output of this code? \nPrint(\"Hello, world!\")\nType your answer using correct lowercase & uppercase: ")

if answer == "NameError" or answer == "nameerror":
  typingPrint("You answered " + answer + ". \n")
  typingPrint("You are correct!\n")
  typingPrint("The output of this code is NameError. \n")
elif answer != "NameError":
  typingPrint("You answered incorrectly. \n")
  typingPrint(answer + " is not NameError. \n")
  typingPrint("Please, review Python exceptions. \n")
else:
  typingPrint("Invalid input \n")


# Wipes the console/screen/output area.
time.sleep(1)  
clearScreen()


# Question #3 
# Added an escape character (\n) to break up the following string into 2 lines.
answer = typingInput("Question #3\nWhat is the output of this code? \nprint(\"Hello, world!\"\nType your answer using correct lowercase & uppercase: ")

if answer == "SyntaxError" or answer == "syntaxerror":
  typingPrint("You answered " + answer + ". \n")
  typingPrint("You are correct!\n")
  typingPrint("The output of this code is SyntaxError. \n")
elif answer != "SyntaxError":
  typingPrint("You answered incorrectly. \n")
  typingPrint(answer + " is not SyntaxError. \n")
  typingPrint("Please, review Python exceptions. \n")
else:
  typingPrint("Invalid input \n")


# Wipes the console/screen/output area.
time.sleep(1)  
clearScreen()


# The end sequence
time.sleep(1)  
typingPrint("Thank you for participating. Good bye.\n")
typingPrint("This screen will clear itself in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)


# Wipes the console/screen/output area.
clearScreen()

