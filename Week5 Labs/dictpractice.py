# Program for practice manipulation of dictionary types
# Author: Gerry Donnelly. 


numbers = {"one" : 1, "two" : 2, "three": 3, "four" : 4, "five": 5}

for x in numbers: # loop to print out the dictionary keys. 
    print(x)


numbers.pop("three") # remove key three and value. 
numbers.popitem() # remove the last key and value. 

numbers["six"] = 6 # add in new keys and values. 
numbers["seven"] = 7

for x in numbers:
    print ("The contents of the dictionary are key: {}, value: {}". format(x, numbers[x])) # print out the updated list of keys and values. 
