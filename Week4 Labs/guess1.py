# Coding For and While Loops, program to check if a number input (guess) matches the hidden number. 
# Author Gerry Donnelly


number = 5 # this is the number to be guessed. 
guess = 0

while guess != number:
        guess = int(input("Please enter a mumber:"))  
        print("Wrong, try again")
print("Well done, the number was {}".format(number))