# Program to generate and print out random fruits from a list. 
# Author: Gerry Donnelly


import random as rd

fruits = ("apple", "pear", "plum", "orange", "bananna", "grape", "lemon", "lime") # List of fruits. 

randfruits = fruits[rd.randint(0,len(fruits)-1)] # Generate a random index for the list and assign to the variable.

print ("A random fruit:{}".format(randfruits))
