"""
Question 015
-------------
Swap two numbers without using a third variable.
-------------
"""
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

# Method 2 : Without Using a third variable

a,b = b,a

print(a,b)


# Method 2 : Using a third variable

# temp = a
# a = b
# b = temp

# print(a)
# print(b)