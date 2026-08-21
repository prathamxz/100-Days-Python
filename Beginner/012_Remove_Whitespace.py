"""
Question 012
-------------
Remove all whitespace from a string.
-------------
"""

string = input("Enter a string: ")

for i in string:
    string = string.replace(" ","")
print(string)