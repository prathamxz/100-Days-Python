"""
Question 023
-------------
Remove duplicate elements from a list.
-------------
"""
lst = [1,2,2,1,3,4,5,3,6,12,13,12,13,16,21,23,24,3,50,50,60]

lst_new = []

for i in lst:
    if i in lst_new:
        pass
    else:
        lst_new.append(i)
print(lst_new)


