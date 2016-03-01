# 2.2-2
# Consider sorting n numbers stored in array A by first finding the smallest element
# of A and exchanging it with the element in A[1]. Then find the second smallest
# element of A, and exchange it with A[2]. Continue in this manner for the first n-1
# elements of A. Write pseudocode for this algorithm, which is known as selection
# sort. What loop invariant does this algorithm maintain? Why does it need to run
# for only the first n -1 elements, rather than for all n elements? Give the best-case
# and worst-case running times of selection sort in theta-notation.


#A = [ 3, 5, 2, 9, 0 ,13, 6]
#B = [13, 3, 5, 2, 9, 0 , 6, 1]
#B = [13, 9, 6, 5, 3, 2 , 1, 0]
#A = [0, 3, 5, 2, 9, 13 , 6, 1]
A = [31, 41, 59, 26, 41, 58]


def selectionSort(A):
	for i in range(len(A)-1):
		index = i
		#Find the ith smallest element
		for j in range(i+1,len(A)):
			if A[j] < A[index]: # should be less than current ithsmallest element
				index = j 
		swap(A,i,index)

def swap(A,i,j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp


print "Array before sorting : {0}".format(A)
selectionSort(A)
print "Array after sorting : {0}".format(A)