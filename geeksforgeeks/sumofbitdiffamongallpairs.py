# http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/ The
# idea is to count differences at individual bit positions. We traverse from 0
# to 31 and count numbers with ith bit set. Let this count be count. There
# would be n-count numbers with ith bit not set. So count of differences at
# ith bit would be count * (n-count) * 2.


def sumBitDifferences(nums):
	sum = 0
	#32bit mainpulation
	for i in range(0,32):
		count = 0
		for j in range(0,len(nums)):
			#print ( nums[j] , 1<<i , nums[j] & (1 << i)) 
			if (nums[j] & (1 << i)):
				count = count +1 # ith bit set so increase count
                # unset bits will be n-count
        sum = sum + (count * (len(nums)-count) * 2)
        print count, sum
	return sum

if __name__ == "__main__" :

	print(sumBitDifferences([1,3,5]))

