# Insertion Sort
# It compares with already existing elements in the left and put it at the right place

A = [ 3, 5, 2, 9, 0 ,13, 6]
#B = [13, 3, 5, 2, 9, 0 , 6, 1]
#B = [13, 9, 6, 5, 3, 2 , 1, 0]
B = [0, 3, 5, 2, 9, 13 , 6, 1]
C = [31, 41, 59, 26, 41, 58]

def insertionsort( A ):
	for i in range(1, len(A)):
		key = A[i] # pickup element from deck
		j = i-1
		# Sort the new element and put it where it belongs
		# Make sure to terminate when A[1..j] is sorted
		while j>=0 and A[j] > key: # Use < for decreasing order
			A[j+1] = A[j]
			j = j-1
		A[j+1] = key


print "Array before sorting : {0}".format(A)
insertionsort(A)
print "Array after sorting : {0}".format(A)

print "Array before sorting : {0}".format(B)
insertionsort(B)
print "Array after sorting : {0}".format(B)

print "Array before sorting : {0}".format(C)
insertionsort(C)
print "Array after sorting : {0}".format(C)
