firstnumber = int(input("Enter the first number:"))
secondnumber = int(input("Enter the second mumber:"))

answer = int(secondnumber // firstnumber)
remainder = secondnumber % firstnumber

print ("{} divided by {} is {} and the remainder is {}".format(secondnumber, firstnumber, answer, remainder))