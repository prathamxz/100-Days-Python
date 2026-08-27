"""
Question 019
-------------
Calculate simple interest given principal, rate, and time.
-------------
"""
# Simple Interest = (Principal × Rate × Time) / 100


def interest():
    a = int(input("Enter Given Principal: "))
    b = int(input("Enter Given Rate: "))
    c = int(input("Enter Given Time: "))
    return a*b*c/100

print(interest())


