# Same as baseConverter but using recursive calls
def toStr(num,base):
	convertString = "0123456789ABCDEF"
	if num < base:
		return convertString[num]
	else:
		return toStr(num//base, base)+convertString[num%base]


print toStr(1453, 16)

print "String value of 10 in different bases"
print toStr(10, 2)
print toStr(10, 8)
print toStr(10, 10)
print toStr(10, 16)
