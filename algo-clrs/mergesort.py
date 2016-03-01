# Merge Sort 
# Divide and Conquer Approach

def merge(A,p,q,r):
	L=A[p:q] 
	R=A[q+1:r]
	print L
	i=0; j=0
	for k in range(p,r) :
		#print "{0} {1}".format(i,j)
		if L[i] <= R[j] :
			A[k] = L[i]
			i=i+1
		else :
			A[k] = R[j]
			j=j+1


def mergesort(A,p,r):
	if(p < r):
		q = (p+r)/2
		mergesort(A,p,q)
		mergesort(A,q+1,r)
		merge(A,p,q,r)


A = [31, 41, 59, 26, 41, 58]

print "Array before sorting : {0}".format(A)
mergesort(A,0,len(A)-1)
print "Array after sorting : {0}".format(A)