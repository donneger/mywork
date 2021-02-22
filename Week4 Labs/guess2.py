# Coding For and While Loops, program to use a random number generator to guess a number. 
# Author Gerry Donnelly

import random as rd

number = 37 # number to be guessed. 

guess = rd.randint(0,100) # randon guesses between 0 and 100. 

while guess != number:
    if guess > number:
        print("Wrong, {} is too high, try again".format(guess))
        guess = rd.randint(0,100) 
    else:
        print("Wrong, {} is too low, try again".format(guess)) 
        guess = rd.randint(0,100)
print("Well done, the number was {}".format(number))


