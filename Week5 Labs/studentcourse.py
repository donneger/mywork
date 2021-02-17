# Program to store students name and courses.
# Author: Gerry Donnelly. 

college = {
    "Name": "Mary", "Modules" : [
        {"Module Name" : "Programming",
        "Grade" : 45
        }, 

        {"Module Name" : "History",
        "Grade" : 99
        }
    ]
    
}

print (college["Name"])
for modules in college["Modules"]:
    print (modules["Module Name"], "\t", modules["Grade"])
