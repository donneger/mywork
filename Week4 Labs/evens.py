# Coding FOR and WHILE Loops, program prints out only the even numbers between 0 and 100 (excl 0)
# Author: Gerry Donnelly

numberto = 100
evennum = 2

while evennum <= numberto:
    if evennum%2 == 0:
        print(evennum) #only print if result is even. 
        evennum +=2
    else:
        evennum +=2



