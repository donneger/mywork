# Coding practice to check out While and For Loops. This program takes in a series of numbers and calculates the average. 
# It prints out the numbers that were input and the average of those numbers. 0 is entered to run the calculation. 
# Author: Gerry Donnelly

numberin = int(input("Please enter your numbers, enter 0 when finished :"))
avlist = [] # set up an empty list. 
while numberin != 0:
    avlist.append(numberin) 
    numberin = int(input("Please enter a number:")) # This loop will repeat until 0 is entered. 
listlen = len(avlist)
avg = sum(avlist)/(listlen)
for num in avlist: # The for loop will print out each of the numbrs in the list. 
    print(num)
print ("The average is", round(avg, 2))