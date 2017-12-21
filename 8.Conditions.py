# Python 3.6.3 lessons - Excercise 8
# Developer - Rahul Rakesh
# Conditions in Python

def getInput():
    evenodd = int(input("Input Number = "))
    while(1):
        if(evenodd % 2 == 0):
            print("Even Number. ")
            break
        else:
            evenodd = int(input("Odd Number. Input Number = "))

getInput()