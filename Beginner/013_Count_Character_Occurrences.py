"""
Question 013
-------------
Count occurrences of a given character in a string.
-------------
"""

string = "Hello, my name is lily. I'm going to london tomorrow with my parents. why are u guys laughing? what time it is in london right now? "
string = string.lower()
count_char = input("Enter character: ").lower()
count_char_total = 0
for i in string:
    if count_char==i:
        # print(i)
        count_char_total+=1

print(count_char_total)
