"""
Question 008
-------------
Print the first n prime numbers.
-------------
"""

num = int(input("Enter how many prime numbers: "))

count = 0
number = 2

while count < num:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number)
        count += 1

    number += 1