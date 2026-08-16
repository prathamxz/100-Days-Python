"""
Question 001
-------------
Check if a given number is even or odd.

Difficulty : Beginner

Example:
Input : 10
Output: Given number is Even.

Time Complexity : O(1)
Space Complexity: O(1)

"""


num = int(input("Enter Your Number:"))

if num % 2 == 0:
    print("Given Number is Even")

else:
    print("Given Number is Odd")