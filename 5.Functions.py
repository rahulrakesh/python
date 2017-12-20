#Python 3.6.3 lessons - Excercise 4
#Developer - Rahul Rakesh
#Functions

"""Python provides a built-in function called len that returns the length of a string, so
the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.
"""

def right_justify(str):
    str_len = len(str)
    max_len = 70
    start_index = max_len - str_len
    
    text = " "
    for i in range(start_index - 1):
     text+=" "
    print(text+str)

right_justify("Hi")
right_justify("rahul")
right_justify("rahul rakesh")
right_justify("rahul rakesh is a good boy")
 