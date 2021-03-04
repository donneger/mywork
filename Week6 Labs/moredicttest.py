D1 = []
D2 = {}
name = "test"

while name != "":
    name = input("Enter Student Name:")
    if name == "":
        break
    D1.append(name)
    course = 0
    grade = 0
    while course != "":
        course = str(input("\tEnter Course:"))
        if course == "":
            break
        grade = input("\tEnter Grade:")  
        D2 = {course:grade}
        D1.append(D2)
        
        
print(D1)
