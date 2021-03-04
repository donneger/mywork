

with open("test.txt", "at") as f:
    f.write("This is and more text written to the file \n")

with open("test.txt", "rt") as f:
    for line in f:
        print("We got: ", line.strip())
    print("success")
