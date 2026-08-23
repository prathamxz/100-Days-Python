"""
Question 014
-------------
Check if two strings are anagrams of each other.
-------------
Hint : 

Two strings are anagrams if:
- They contain the same characters.
- Each character appears the same number of times.
- The order of the characters doesn't matter.

listen ---> silent ✅
cat ---> act ✅

"""

lst1 = input("String 1: ").lower()
lst2 = input("String 2: ").lower()

lst1_char = []
lst2_char = []

for i in lst1:
    lst1_char+=i
for i in lst2:
    lst2_char+=i

lst1_char.sort()
lst2_char.sort()

if lst1_char==lst2_char:
        print("strings are anagrams of each other")



