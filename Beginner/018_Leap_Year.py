"""
Question 018
-------------
Check whether a given year is a leap year.
-------------
"""

year = int(input("Enter Your Year: "))

if year % 400 == 0:
    print(f"The Given Year {year} is a Leap Year")
elif year % 100 == 0:
    print(f"The Given Year {year} is Not a Leap Year")
elif year % 4 == 0:
    print(f"The Given Year {year} is a Leap Year")
else:
    print(f"The Given Year {year} is Not a Leap Year")