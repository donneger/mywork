# Lab 5 Programs, Tuples. Program to print out the summer months from a Tuple. 
# Author: Gerry Donnelly

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

summermonths = months[4:7] # select the 5th, 6th and 7th members of the tuple. 

for month in summermonths:
    print (month)