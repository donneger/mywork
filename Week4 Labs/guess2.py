# Coding For and While Loops
# Author Gerry Donnelly

import random as rd

number = 37

guess = rd.randint(0,100)

while guess != number:
    if guess > number:
        print("Wrong, too high, try again")
        guess = rd.randint(0,100) 
    else:
        print("Wrong, too low, try again") 
        guess = rd.randint(0,100)
print("Well done, the number was {}".format(number))


