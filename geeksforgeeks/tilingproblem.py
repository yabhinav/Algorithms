# Count number of ways to fill a n x 4 grid using 1 x 4 tiles
# http://www.geeksforgeeks.org/count-number-of-ways-to-fill-a-n-x-4-grid-using-1-x-4-tiles/
   # count(n) = 1 if n = 1 or n = 2 or n = 3   
   # count(n) = 2 if n = 4
   # count(n) = count(n-1) + count(n-4) 
# This recurrence is similar to Fibonacci Numbers and can be solved using Dynamic programming.
def count(n):
	#Create a table to store results of subproblems
        #dp[i] stores count of ways for i x 4 grid.
    dp = [0]*(n+1)
 
    #Fill the table from d[1] to dp[n]
    for i in range(1,n+1) :
        #Base cases
        if (i >= 1 and  i <= 3) :
            dp[i] = 1
        elif (i==4) :
            dp[i] = 2 
        else :
            #dp(i-1) : Place first tile horizontally
            #dp(n-4) : Place first tile vertically
            #          which means 3 more tiles have
            #          to be placed vertically.
            dp[i] = dp[i-1] + dp[i-4]
    print dp
    return dp[n]


print count(5)