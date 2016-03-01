# 2.3-7
# Describe a T(n lg n)-time algorithm that, given a set S of n integers and another integer x, 
# determines whether or not there exist two elements in S whose sum is exactly x.

def sum_exists(S, x): # nlogn + nlogn
	merge_sort(S, 0, len(S) - 1) # nlogn
	for a in range(len(S) - 1): # n times
	    b = binary_search(S[a + 1:], x - S[a]) # logn
	    if b is not None:
	        return True
	return False


def merge_sort(A, p, r): # n logn
	if p < r:
	    q = (p + r)//2
	    merge_sort(A, p, q)
	    merge_sort(A, q + 1, r)
	    merge(A, p, q, r)


def merge(A, p, q, r):    # See Exercise 2.3-2
	n1 = q - p + 1
	n2 = r - q
	L = [A[p + i] for i in range(n1)]
	R = [A[q + j + 1] for j in range(n2)]
	i = j = 0
	for k in range(p, r + 1):
	    if j >= len(R) or (i < len(L) and L[i] <= R[j]):
	        A[k] = L[i]
	        i = i + 1
	    else:
	        A[k] = R[j]
	        j = j + 1


def binary_search(A, v):    # See Exercise 2.3-5
	low = 0
	high = len(A) - 1
	mid = (low + high)//2
	while low <= high and A[mid] != v:
	    if A[mid] < v:
	        low = mid + 1
	    else: high = mid - 1
	    mid = (low + high)//2
	if low > high:
	    return None
	else: return mid


print sum_exists([1,3,5,7,8,0,2], 1)
print sum_exists([1,3,5,7,8,2], 1)