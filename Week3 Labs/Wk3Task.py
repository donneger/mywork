strin = input("Enter a text string: ")

strlen = len(strin)

strout = strin[strlen::-2]

print("Input Text :\t{}\nOutput Text:\t{}".format(strin, strout))