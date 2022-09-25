import os
import math



filename = "gerry.txt"

if(os.path.exists(filename)):
    print("file exists")
else:
    with open("gerry.txt", "x") as f:
        print("just created gerry")