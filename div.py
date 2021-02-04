firstnumber = int(input("Enter the first number:"))
secondnumber = int(input("Enter the second mumber:"))

answer = secondnumber // firstnumber
remainder = secondnumber % firstnumber

print ("{} divided by {} is {} and remainder {}".format(secondnumber, firstnumber, answer, remainder))