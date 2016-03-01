# Python program to find maximum contiguous subarray
# Exercise 4.1-5

def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print"Maximum contiguous sum is" , maxSubArraySum(a,len(a))

Arr = [20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
                    34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49, 
                    3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67, 
                    -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34, 
                    88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9, 
                    2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55, 
                    23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56, 
                    -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88, 
                    -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76];
print"Maximum contiguous sum is" , maxSubArraySum(Arr,len(Arr))