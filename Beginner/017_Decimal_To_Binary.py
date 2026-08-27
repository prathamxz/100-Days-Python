"""
Question 017
-------------
Convert a decimal number into binary.
-------------
"""

def binary(num):
    if num == 0:
        return

    binary(num // 2)
    print(num % 2, end="")


num = int(input("Enter a number: "))

if num == 0:
    print(0)
else:
    binary(num)