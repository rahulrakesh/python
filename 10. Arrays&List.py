"""
#Python 3.6.3 lessons - Excercise 1
#Developer - Rahul Rakesh
#Arrays and Lists
"""

mygrocerylist = ["bread", "egg", "milk", "carrots", "lettuce"]

def printstring():
    grocerylist = "eggs,bread,milk,carrots,lettuce"
    print(grocerylist)

def printarray():    
    print(mygrocerylist)
    print("Length of the array = ",+len(mygrocerylist))
    print()
    

def printArrayOnebyone():
    for i in range(0,len(mygrocerylist)):
       print(mygrocerylist[i])


printstring()
printarray()
#printArrayOnebyone()

mygrocerylist.append("potato")
mygrocerylist.append("sugar")
del mygrocerylist[0]

printArrayOnebyone()

def hybridArrays():
    hybridArray = [1,2,3,"milk","sugar","rice"]
    print(">>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<")
    for i in range(0,len(hybridArray)):
        print(hybridArray[i])

hybridArrays()