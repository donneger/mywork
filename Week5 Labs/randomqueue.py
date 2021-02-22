# Program to generate a list of random numbers and print out the first number of the list, remove it from the list print out the list. 
# Keep doing this until the list is emptied. 

# Author: Gerry Donnelly.

import random as rd

randlist = [] #set up the empty list. 

numberofnumbers = 10 # This will be the length of the list. 
rangeto = 100 # wil generate random numbers between 0 and 100. 

for i in range(numberofnumbers): # loop, in this case 10 times. 
    randlist.append(rd.randint(0,rangeto)) # append the random number to the list. 
print("The queue is {}".format(randlist))
while len(randlist) != 0:
    print ("The current number is {} and the queue is {}".format(randlist.pop(0), randlist)) # use the pop in here to remove the first number from the list each time it loops. 
print("The queue is now empty")
   
