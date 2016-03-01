# 2.1-4
# Consider the problem of adding two n-bit binary integers, stored in two n-element
# arrays A and B. The sum of the two integers should be stored in binary form in
# 2.2 Analyzing algorithms 23
# an .n C 1/-element array C. State the problem formally and write pseudocode for
# adding the two integers.

def binarysum( A, B):
	carry = 0
	C = [0]*(len(A)+1)

	for i in range(0, len(A)-1) :
		C[i] = (A[i]+B[i]+carry)%2 #remainder
		carry = (A[i]+B[i]+carry)/2 #quotient

	C[len(A)] = carry
	return C


print binarysum([0,1,1,0], [1,0,1,1] )