text = str(input("Please enter a string: "))

strcntin = len(text)

text = text.strip().casefold()

strcntout = len(text)

print ("We reduced the length of the string from {} to {} characters".format(strcntin, strcntout))