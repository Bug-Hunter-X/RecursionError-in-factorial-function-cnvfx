def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) 
print(factorial(0))
try:
    print(factorial(-1))
except ValueError as e:
    print(f"Error: {e}") #This will now gracefully handle negative input