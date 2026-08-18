"""
Question 006
-------------
Find the factorial of a number using recursion.
-------------
"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num - 1)


num = int(input("Enter a number: "))

result = factorial(num)

print(f"Factorial of {num} is {result}")
    
