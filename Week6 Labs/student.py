# Week 6 Lab Program - Student Management Program to add, abd view student, courses and grades. 
# Author: Gerry Donnelly




def menustart ():
        print ("What would you like to do? \n\t (A)dd a New Student \n\t (V)iew Students \n\t (Q)uit")
        selection =  input("Type one letter from menu above:")
        while selection not in ("a", "v", "q"):
                print ("Please try again, input not valid, please input a, v or q")
                selection =  input("Type one letter from menu above:")
        return (selection)

def addstudentnm(students):
        newstudents = {}
        newstudents["Name"] = input("Enter Student Name:")
        newstudents["Courses"] = courses()
        students.append(newstudents)
        return students

def courses():
        newmod=[]
        modnm = str(input("\tEnter Course:")).strip()
        while modnm != "":
                newmods = {}
                newmods["Course"] = modnm
                newmods["Grade"] = input("\tEnter Grade:")  
                newmod.append(newmods)
                modnm = str(input("\tEnter Course:")).strip()
        return newmod

Students = []
selection = menustart()

while selection != "q":
        if (selection) == "a":  
                print (Students)
                addstudentnm(Students)
        elif (selection) == "v":
                print ("View Student")
        elif (selection) == "q":
                print ("quit")        
        selection = menustart()
