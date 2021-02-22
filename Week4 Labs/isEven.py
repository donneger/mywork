# Coding practice for If Statements, program to check if a number input is odd or even. 
# Author: Gerry Donnelly

number = int(input("Please enter a number:"))

if (number%2) == 0:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))

