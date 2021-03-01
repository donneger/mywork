D = {'Mary': {'Course': 'History', 'Grade': 20},
     'John': {"Course": 'Geography', "Grade": 40},
     'Tom': {"Course": 'Maths', "Grade": 60}}

D['Gerry'] = {"Course": 'French', "Grade": 80}
D['Fiona'] = {"Course": 'German', "Grade": 100}


for student, courses in D.items():
   print("Name:", student)
   for course in courses:
        print("\t", course, courses[course])