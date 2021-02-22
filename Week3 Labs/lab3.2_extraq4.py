# Program to conver dollars to cents. 
# Gerry Donnelly

dolin = float(input("Please enter an amount: "))

dolout = abs(round(dolin*100)) # use abs in case a neagtive value is input.

print ("You entered {} dollar, that amount in cent is: {}".format(dolin, dolout))