# Manager rated N employees by score, if the next employee has more score give
# him more chocolate. Minimum 1 chocolate was given. what is the minimum
# chocolates manager should carry to distribute

def findMin(score, n):
	count=1
	prev=1
	for i in range(1,n) :
		if score[i] > score[i-1] :
			count = count+prev+1 # give 1 chocolate more than prev employee
		else:
			count = count+1 # give only one chocolate to i employee
			prev =1

	return count

print findMin([1,1,1,1],4)
print findMin([1,0,1,1],4)
print findMin([0,1,0,1],4)
print findMin([1,2,3,4],4)
print findMin([3,5,6,8],4)



