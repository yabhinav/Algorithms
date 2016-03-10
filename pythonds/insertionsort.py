# The insertion sort, although still O(n2), works in a slightly different way.
# It always maintains a sorted sublist in the lower positions of the list.
# Each new item is then 'inserted' back into the previous sublist such that
# the sorted sublist is one item larger.

def insertionsort(alist):
	for i in range(1,len(alist)):
		temp = alist[i]
		j = i
		while j>=0 and alist[j-1] > temp:
			alist[j],alist[j-1] = alist[j-1],alist[j]
			j = j-1
		alist[j] = temp

alist = [54,23,46,93,17,77,44,50,17]
insertionsort(alist)
print alist
