# Coding For and While Loops
# Author Gerry Donnelly


number = 5
guess = 0

while guess != number:
        guess = int(input("Please enter a mumber:"))  
        print("Wrong, try again")
print("Well done, the number was {}".format(number))