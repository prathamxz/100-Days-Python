"""
Question 022
-------------
Print all odd numbers in a list.
-------------
"""

lst = [0,1,2,3,4,5,12,13,22,43,44]
new_list = []
for i in lst:
    if i%2 != 0:
        new_list.append(i)
print(new_list)