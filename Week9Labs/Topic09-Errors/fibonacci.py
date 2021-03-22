
import logging as lg
lg.basicConfig(level=lg.DEBUG)

def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError("Number must be >0")
    a = 0
    b = 1
    fibsequence = []
    for i in range(1, number):
        fibsequence.append(b)
        a , b = b , a + b
        #a = b
        #b = a+b
    lg.debug("%d: %s", number, fibsequence)
    return []

if __name__ == "__main__":
    return7 = [1,1,2,3,5,8]
    return11 = [1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return for 0'
    assert fibonacci(1) == [0], 'incorrect return for 1'


    print("all good")