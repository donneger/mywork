numbers = {"one" : 1, "two" : 2, "three": 3, "four" : 4, "five": 5}

for x in numbers:
    print(x)


numbers.pop("three")
numbers.popitem()

numbers["six"] = 6
numbers["seven"] = 7

for x in numbers:
    print ("The contents of the dictionary are key: {}, value: {}". format(x, numbers[x]))
