numbers = {
    "one" : {
    "first": "A", 
    "second" : "B"
    }, 
    
    "two" : {
        "Third" : "C",
        "Fourth" : "D"
    },

    "three": {
        "Fifth" : "E", 
        "Sixth" : "F"
    }
}
#print (numbers)
#print (numbers.get("three"))

for x, y in numbers.items():
    print(x, "\n", y, len(numbers))