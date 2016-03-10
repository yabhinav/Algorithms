
def removeWhite(s):
	return "".join(c for c in s if c not in ('!','.',':','?','"',"'"," "))

def isPal(s):
	print s
	if len(s) <=1 :
		return True
	else:
		return (s == reverse(s))

def reverse(s):
	if len(s)>1:
		return reverse(s[1:])+s[0]
	elif len(s)==1:
		return s[0]

print isPal(removeWhite("hello"))
print(isPal(removeWhite("")))
print(isPal(removeWhite("madam i'm adam")))
