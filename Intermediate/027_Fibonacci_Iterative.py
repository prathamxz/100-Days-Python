"""
Question 027
-------------

Find the Fibonacci series up to n terms, using an iterative method.

Example:
Input:
5

Output:
0 1 1 2 3

-------------

Time Complexity: O(n)
Space Complexity: O(1)
"""

num = int(input("Enter your Number: "))

first = 0
second = 1

for i in range(num):
    print(first, end=" ")

    next_num = first + second
    first = second
    second = next_num