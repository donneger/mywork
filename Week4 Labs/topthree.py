# Week 4 Practice Coding, program to generate a number of random numbers and output the top 3 in reverse order. 
# Author: Gerry Donnelly

import random as rn

numlist = [] # set up empty list to hold the numbers.
counter = int(input("How many random numbers do you want: "))
for x in range(counter): #Loop repeats for number of random numbers requested. 
    randout = (rn.randint(1,100)) # generate randonm numbers between 0 and 100. 
    numlist.append(randout)
print("The {} random numbers are {}".format(counter, numlist))
numlist.sort(reverse=True)   
print ("The top 3 are {}".format(numlist[0:3]))
