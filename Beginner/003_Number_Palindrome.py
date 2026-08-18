"""
Question 003
-------------
Check whether a given number is a palindrome.
-------------
"""
# Hint --- A palindrome number is a number that reads the same forwards and backwards.

"""
Question 003
------------
Check whether a given number is a palindrome.

Difficulty: Beginner
"""

num = int(input("Enter a number: "))

original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")
