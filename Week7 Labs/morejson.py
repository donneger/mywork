

import json

with open("student.json", "rt") as f:
    readcourse = json.load(f)   
    print (readcourse["name"])


course = {"name" : "Gerry", "Course": "History", "Grade": 99}

with open("student.json", "wt") as f:
    json.dump(course, f)


