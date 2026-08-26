"""
Question 016
-------------
Find the sum of digits of a number using recursion.
-------------
"""

def sum_digits(num):
    # Base case
    if num == 0:
        return 0

    # Recursive case
    return (num % 10) + sum_digits(num // 10)


number = int(input("Enter a Number: "))
print("Sum of digits:", sum_digits(number))