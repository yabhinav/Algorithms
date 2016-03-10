from basic.Stack import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,8))
print(baseConverter(25,12))
print(baseConverter(25,16))

print "Deicmal Value :10 in different bases"
print baseConverter(10, 2)
print baseConverter(10, 8)
print baseConverter(10, 10)
print baseConverter(10, 16)