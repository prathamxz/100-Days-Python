"""
Question 011
-------------
Count the number of vowels in a given string.
-------------
"""

string = input("please enter a string: ")
string = str.lower()
str_count =0

for i in string:
    if i in "aeiou":
        str_count += 1

print(str_count)

