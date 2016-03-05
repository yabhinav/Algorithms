from basic.Stack import Stack

# The Divide by 2 algorithm assumes that we start with an integer greater than 0. 
# A simple iteration then continually divides the decimal number by 2 and keeps track of the remainder. 
# The first division by 2 gives information as to whether the value is even or odd. An even value will have a remainder of 0. 
# It will have the digit 0 in the ones place. 
# An odd value will have a remainder of 1 and will have the digit 1 in the ones place
# The decimal number 233 and its corresponding binary equivalent 111010012


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))
print(divideBy2(1))
