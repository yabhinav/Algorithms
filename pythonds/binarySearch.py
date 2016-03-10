def binarySearch(alist,item):
	if len(alist) == 0:
		return False
	mid = len(alist)//2

	if alist[mid] == item:
		return True
	elif alist[mid] > item:
		binarySearch(alist[:mid], item)
	else:
		binarySearch(alist[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
 