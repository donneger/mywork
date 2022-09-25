import csv


filename = "employees.csv"

with open(filename, "rt") as fname:
    rd_data = csv.reader(fname, delimiter = ",")
    next(rd_data)
    
    count = 0
    for row in rd_data:
        email = row[8]
        x = email.find("@")
        count +=1
        print(email[x:])
    print(count)
    
    