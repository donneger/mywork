# More If statement Coding, program calculate the the grade level based on the grade mark input. 
# Author: Gerry Donnelly

grade = int(input("Please enter the grade:"))

if grade < 40:
    print ("Your Grade is under 40% == FAIL")
elif grade < 50:
    print ("Your grade is a Pass")
elif grade < 60:
    print ("Your grade is Merit 2")
elif grade < 70:
    print ("Your grade is Merit 1")
else:
    print ("Your Grade is Distinction")