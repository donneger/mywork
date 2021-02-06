import random as rn

counter = int(input("How many random numbers do you want: "))
for x in range(counter):

    randout = (rn.randint(1,10))

    print (randout, end = " ")

