"""
Question 007
-------------
Check whether a number is prime.
-------------
"""

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")