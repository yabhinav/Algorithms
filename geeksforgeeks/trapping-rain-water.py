# http://www.geeksforgeeks.org/trapping-rain-water/ An Efficient Solution is
# to prre-compute highest bar on left and right of every bar in O(n) time.
# Then use these pre-computed values to find the amount of water in every
# array element.

def findwater(alist):
    n = len(alist)
    maxleft  = [alist[0]]*n
    maxright = [alist[n-1]]*n
    water=0
    for i in range(n):
        maxleft[i] = max(maxleft[i-1], alist[i])
    
    for i in range(n-1):
        maxright[i] = max(maxright[i+1], alist[i])
    
    print maxleft, maxright

    for i in range(0,n):
        water = water+min(maxleft[i],maxright[i])-alist[i]
    
    return water
    

print findwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) #6
print findwater([3, 0, 0, 2, 0, 4]) #10
print findwater([2, 0, 2]) #2
