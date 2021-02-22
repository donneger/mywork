# Program to check use of floor and ceiling. 
# Author: Gerry Donnelly

import math

floatin = float(input("Input a Float number: "))

flooroutf = math.floor(floatin) # use floor to get nearest lower integer.
flooroutc = math.ceil(floatin) # use ceil to get nearest higher integer. 

print ("{} floored is: {}".format(floatin, flooroutf))
print ("{} ceiling is: {}".format(floatin, flooroutc))