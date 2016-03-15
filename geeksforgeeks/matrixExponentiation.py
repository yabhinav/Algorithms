# Matrix Exopnentiation
# http://www.geeksforgeeks.org/matrix-exponentiation/


# // Return n'th term of a series defined using below
# // recurrence relation.
# // f(n) is defined as
# //    f(n) = f(n-1) + f(n-2) + f(n-3), n>=3
# // Base Cases :
# //    f(0) = 0, f(1) = 1, f(2) = 1
def findNTerm(n):

	F = [[1,1,1],[1,0,0],[0,1,0]] # F(n) = F(n-1) + F(n-2) + F(n-3), n >= 3

	return power(F, n-2)

def power(F, n):
	M = [[1,1,1],[1,0,0],[0,1,0]] 

	# // Multiply it with initial values i.e with
	#// F(0) = 0, F(1) = 1, F(2) = 1
	if n==1 :
		return F[0][0] + F[0][1]

	power(F, n/2)

	multiply(F, F)

	if (n%2 != 0) :
	    multiply(F, M)

	# // Multiply it with initial values i.e with
	# // F(0) = 0, F(1) = 1, F(2) = 1
	return F[0][0] + F[0][1]

# // A utility function to multiply two matrices
# // a[][] and b[][].  Multiplication result is
# // stored back in b[][]
def multiply( a, b) :
    # // Considering an auxiliary matrix to store elements of
    # // the matrix
    mul = [[],[],[]]
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3) :
                mul[i][j] += a[i][k]*b[k][j]

    # // storing the muliplication resul in a[][]
    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]  #// Updating our matrix


if __name__ == "__main__":
	print findNTerm(5)