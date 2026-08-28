"""
Question 025
-------------
Merge two dictionaries.
-------------
"""

dict_1 = {
    "Virat" : 100,
    "Dhoni" : 32,
    "Sachin" : 92,
    "Yuvraj" : 98,
}

dict_2 = {
    "Shikhar" : 55,
    "Ishan" : 12,
    "Gill" : 52,
    "Vaibhav" : 95,
}

dict_new = {}
for i in dict_1:
    dict_new[i] = dict_1[i]

for i in dict_2:
    dict_new[i] = dict_2[i]

print(dict_new)

