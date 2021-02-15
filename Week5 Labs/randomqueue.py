import random as rd

randlist = []

numberofnumbers = 10
rangeto = 100

for i in range(numberofnumbers):
    randlist.append(rd.randint(0,rangeto))
print("The queue is {}".format(randlist))
while len(randlist) != 0:
    print ("The current number is {} and the queue is {}".format(randlist.pop(0), randlist))
print("The queue is now empty")
   
