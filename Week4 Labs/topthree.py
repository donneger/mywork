# Week 4 Practice Coding
# Author: Gerry Donnelly

import random as rn

numlist = []
counter = int(input("How many random numbers do you want: "))
for x in range(counter):
    randout = (rn.randint(1,100))
    numlist.append(randout)
print("The 10 random numbers are {}".format(numlist))
numlist.sort(reverse=True)   
print ("The top 3 are {}".format(numlist[0:3]))
