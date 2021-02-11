# Coding practice to While and For Loops
# Gerry Donnelly

numberin = int(input("Please enter a number:"))
avlist = []
while numberin != 0:
    avlist.append(numberin) 
    numberin = int(input("Please enter a number:"))
listlen = len(avlist)
avg = sum(avlist)/(listlen)
for num in avlist:
    print(num)
print ("The average is", round(avg, 2))