# Program to calculate Square Root using Newtons Method.
# 

def sqroot (number, accuracy, test = 1, root= 0):
    
    guess = number
    while test > accuracy:
        root = (guess + number/guess)/2
        test = abs(root - guess)
        if test < accuracy:
            print("The number input was: {} The square root of the number is: {}".format(number, root))
        guess = root 


number = int(input("Please  input the number to be rooted:"))
t = float(input("Please neter the accuracy level desired in %: "))
accuracy = 1-(t/100)

sqroot(number, accuracy)

