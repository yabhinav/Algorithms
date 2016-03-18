# https://www.careercup.com/question?id=5104572540387328
# Given a sorted array of integers, write a function that will return the number with the biggest number of repetitions.
# (Asked to refine the solution to be more efficient)

def findMaxRepElement(alist):
	count =1 ; maxcount=1
	maxelement=alist[0] ;element = alist[0]

	for i in range(1,len(alist)):
		if alist[i] == element :
			count+=1
			if count >= len(alist):
				return element
			elif count > maxcount :
				maxelement = alist[i]
				maxcount = count
		else :
			element = alist[i]
			count =1
			
	if count > maxcount : #If last element has more count
		return element
	else:
		return maxelement


print( findMaxRepElement([1,1,2,2,3,3,5,5,5,5,5])) 
print( findMaxRepElement([1,1,1,1,1,1,1,5,5,5,5])) 