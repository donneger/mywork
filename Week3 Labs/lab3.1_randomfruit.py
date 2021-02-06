import random as rd

fruits = ("apple", "pear", "plum", "orange", "bananna", "grape", "lemon", "lime")

index = rd.randint(0,len(fruits)-1)

fruits = fruits[index]

print ("A random fruit:{}".format(fruits))
