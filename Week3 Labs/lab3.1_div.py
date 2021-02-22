# Program to divide one number by the other, print out the integer result and the remainder. 
# Author: Gerry Donnelly

# Enter the Numbers
firstnumber = int(input("Enter the first number:"))
secondnumber = int(input("Enter the second mumber:"))

answer = int(secondnumber // firstnumber) # This give the integer result.
remainder = secondnumber % firstnumber # This gives the remainder,

# Print out the results. 
print ("{} divided by {} is {} and the remainder is {}".format(secondnumber, firstnumber, answer, remainder))