# bubble sort makes multiple passes through a list. It compares adjacent items
# and exchanges those that are out of order. Each pass through the list places
# the next largest value in its proper place. In essence, each item 'bubbles' up
# to the location where it belongs.

def bubblesort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1]=alist[i+1],alist[i] #swap

alist = [54,23,46,93,17,77,44,50,17]
bubblesort(alist)
print alist