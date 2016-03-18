# Find max ways to score n with 1 ,2 4, 6 such that there are no three consecutive boundaries
# Google Round1 Interview 
# Validity not known

def findways(n) :
	alist = [0]*(n+1)
	alist[0] = 1

	for i in range(1,n+1):
		alist[i] += alist[i-1]
	# 2,3,4,5,6,8,8,10,12 are possible runs for every 2 balls
	for i in range(2,n+1):
		alist[i] += 2*alist[i-2]
	for i in range(3,n+1):
		alist[i] += 2*alist[i-3]
	for i in range(4,n+1):
		alist[i] += 2*alist[i-4]
	for i in range(5,n+1):
		alist[i] += 2*alist[i-5]
	for i in range(6,n+1):
		alist[i] += 2*alist[i-6]
	for i in range(8,n+1): # 2+6 , 4+4 hence double
		alist[i] += 4*alist[i-8]
	for i in range(10,n+1):
		alist[i] += 2*alist[i-10]
	for i in range(12,n+1):
		alist[i] += 2*alist[i-12]

	return alist[n]


print findways(1)
print findways(2)
print findways(3)
print findways(4)
print findways(6)
print findways(10)