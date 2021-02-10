# Coding For and While Loops
# Author Gerry Donnelly


number = 5
guess = 0

while guess != number:
    if guess > number:
        print("Wrong, too high, try again")
        guess = int(input("Please enter a mumber:"))  
    else:
        print("Wrong, too low, try again") 
        guess = int(input("Please enter a mumber:"))    
print("Well done, the number was {}".format(number))