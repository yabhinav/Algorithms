# BubbleSort
# It works by repeatedly swapping adjacent elements that are out of order.


def bubbleSort(A):
	for passnum in range(len(A)-1,0,-1):
	        for i in range(passnum):
	            if A[i]>A[i+1]:
	                temp = A[i]
	                A[i] = A[i+1]
	                A[i+1] = temp

alist = [31, 41, 59, 26, 41, 58]
bubbleSort(alist)
print(alist)
