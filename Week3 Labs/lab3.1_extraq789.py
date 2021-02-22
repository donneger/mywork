# Program to test variable types.
# Author: Gerry Donnelly


message1 = "I have eaten " + str(99) + " burritos." #convert the 99 to a string, error otherwise

message2 = int(125/12) # int type

message3 = str(125/12) # string type

message4 = round(125/12,2) # float type

# Print out each variable. 
print (message1)
print (message2)
print (message3)
print (message4)
# variable names begining with an integer are not allowed. 
#int, float, str.