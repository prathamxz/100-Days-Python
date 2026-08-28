"""
Question 026
-------------
Find the common elements between two lists.
-------------
"""

lst1 = [1,2,3,4]

lst2 = [3,4,5,7]

lst_new = []

for i in lst1:
    if i in lst2:
        lst_new.append(i)

print(lst_new)
        