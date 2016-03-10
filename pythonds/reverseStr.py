
def reverse(s):
	if len(s)>1:
		return reverse(s[1:])+s[0]
	elif len(s)==1:
		return s[0]
	else :
	  return ""

print reverse("hello")


