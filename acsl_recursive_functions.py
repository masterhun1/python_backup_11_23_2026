# Find f(90) given: 

def f(x):
    if (x % 3 == 0) and (x % 2 == 1):
        return 2 * f(x/3) - 1
    elif (x % 2 == 0):
        return -1 * f(x/2) + 2
    else:
        return x + 4 

        
print(f(90))

print(f(5))
