# Improvement of BubbleSort is that swap is only done once every n-1
# comparision
def selectionsort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		maxposition = 0
		for i in range(1,fillslot+1):
			if alist[i] > alist[maxposition]:
				maxposition = i
		#swap value at max position to its sorted position	
		alist[maxposition],alist[fillslot]=alist[fillslot],alist[maxposition]

alist = [54,23,46,93,17,77,44,50,17]
selectionsort(alist)
print alist