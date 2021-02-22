# Program to check using a string index to generate a substring, in this case every second character starting with the last character
# and same starting with the first character. 

strin = input("Enter a text string: ")

strlen = len(strin)

strout = strin[strlen::-2] # in the case -2 specifices a step of 2 characters starting with the last character. 

print("Input Text :\t{}\nOutput Text:\t{}".format(strin, strout))

strout1 = strin[0:strlen:2] # in the case 2 specifices a step of 2 characters starting with the first character. 

print("Input Text :\t{}\nOutput Text:\t{}".format(strin, strout1))
