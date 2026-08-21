"""
Question 011
-------------
Count the number of vowels in a given string.
-------------
"""

string = input("Please enter a string: ").lower()

str_count =0

for i in string:
    if i in "aeiou":
        str_count += 1

print(str_count)

