"""
Question 010
-------------
Find the second largest number in a list.
-------------
"""

lst = [2,3,5,7,11,1,12,19,4]

largest = lst[0]
second_largest = lst[0]

for i in lst:
    if i > largest:
        largest = i

for i in lst:
    if i > second_largest and i < largest:
        second_largest=i

print("Second Largest: ",second_largest)
#print("Largest: ",largest)