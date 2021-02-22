# Program to generate and print out random numbers. 
# Author: Gerry Donnelly


import random as rn # import random module. 

counter = int(input("How many random numbers do you want: ")) # user can input how many randon numbers are required. 

# Loop runs for the number of random numbers user has input. 
for x in range(counter): 

    randout = (rn.randint(1,10)) # This generate a random number between 1 an 10. 

    print (randout, end = " ")

