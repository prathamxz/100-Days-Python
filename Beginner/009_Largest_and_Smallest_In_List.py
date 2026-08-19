"""
Question 009
-------------
Find the largest and smallest number in a list.
-------------
"""

lst = [2,3,5,7,11,1,12,19,4]

smallest= lst[0]
largest= lst[0]

for i in lst:
    if i<smallest:
        smallest=i

    if i > largest:
        largest=i

print("Smallest:", smallest)
print("Largest:", largest)


### Another approach --'''
'''
-------------
print(min(lst))
print(max(lst))
-------------
'''

    