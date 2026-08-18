"""
Question 004
-------------
Check whether a given string is a palindrome.
-------------
"""
# Hint --- A palindrome string is a string that reads the same forwards and backwards.

string = input("Enter your string: ")

if string == string[::-1]:
    print("Is Palindrome")
else:
    print("Not Palindrome")