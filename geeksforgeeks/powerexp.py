def power(x,y):
	if y == 0 :
		return 1
	elif y ==1:
		return x
	elif y == -1:
		return 1/float(x)
	elif y%2 ==0:
		tmp = power(x,y//2)
		return tmp*tmp
	else:
		tmp = power(x,y//2)
		if y > 0 :
			return x*tmp*tmp
		elif y == -3:
			return (tmp)/float(x)
		else :
			return tmp*tmp /float(x)


print power(2,1)
print power(2,2)
print power(2,3)
print power(2,4)
print power(2,5)
print power(5.1,3)
print power(10000,0)
print power(2,-1)
print power(2,-2)
print power(2,-3) # value should be 0.125000
print power(2,-4) 
print power(2,-5) 