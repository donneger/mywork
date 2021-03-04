D = {'Mary': {'Courses': {'History' : 20, "Maths" : 70, "French" : 68}}}


for student, courses in D.items():
   print("Name:", student)
   for course, grade in courses.items():
        print("\t", course, grade, "\n")