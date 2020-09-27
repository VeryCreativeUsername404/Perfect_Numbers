import math

def isitperfect(number):
    listofdivisors = []
    stopnumber = math.ceil(number / 2) + 1
    for x in range(1, stopnumber):
        if number%x == 0:
            listofdivisors.append(x)

    
    if listofdivisors:
        thesum = sum(listofdivisors)
        if thesum == number:
            return True

    return False

for number in range(1, 35000000):
    if number%1000 == 0:
        print('I\'m now at: ' + str(number))
    if isitperfect(number):
        print(str(number) + ' is a perfect number.')