"""
Question 024
-------------
Reverse a list without using the built-in reverse() method.
-------------
"""

lst = [16, 21, 23, 24, 3, 50, 2, 12, 13, 22, 43, 44, 1]

lst_new = []

for i in range(len(lst) - 1, -1, -1):
    lst_new.append(lst[i])

print(lst_new)