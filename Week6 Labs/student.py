# Week 6 Lab Program - Student Management Program to add, abd view student, courses and grades. 
# Author: Gerry Donnelly


print ("What would you like to do? \n\t (a) Add a New Student \n\t (v) View Students \n\t (q) Quit")
x =  input("Type one letter from menu above:")

while x not in ("a", "v", "q"):
        print ("Please try again, input not valid, please input a, v or q")
        x =  input("Type one letter from menu above:")

if (x) == "a":
         print ("Add a new student")
elif (x) == "v":
         print ("View Student")
elif (x) == "q":
         print ("quit")        






















""" student = {
"name":"Mary",
"modules": [
{
"courseName":"Programming",
"grade": 45
},
{
"courseName":"History",
"grade":99
}
]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"])) """