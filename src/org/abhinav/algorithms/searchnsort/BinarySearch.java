package org.abhinav.algorithms.searchnsort;


/*
 * Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

A simple approach is to do linear search, i.e., start from the leftmost element of arr[] and one by one compare x with each element of arr[], if x matches with an element, return the index. If x doesn’t match with any of elements, return -1.

// Linearly search x in arr[].  If x is present then return its 
// location,  otherwise return -1
int search(int arr[], int n, int x)
{
    int i;
    for (i=0; i<n; i++)
        if (arr[i] == x)
         return i;
    return -1;
}
The time complexity of above algorithm is O(n).

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Logn). We basically ignore half of the elements just after one comparison.
1) Compare x with the middle element.
2) If x matches with middle element, we return the mid index.
3) Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4) Else (x is smaller) recur for the left half.

Following are both Iterative and recursive BinarySearch algorithms

Time Complexity:
The time complexity of Binary Search can be written as

T(n) = T(n/2) + c 
The above recurrence can be solved either using Recurrence T ree method or Master method. It falls in case II of Master Method and solution of the recurrence is \Theta(Logn).

Auxiliary Space: O(1) in case of iterative implementation. In case of recursive implementation, O(Logn) recursion call stack space.

Algorithmic Paradigm: Divide and Conquer
 */
public class BinarySearch {
	
	public static int iterativeBinarySearch(int[] array, int l, int r, int x)
	{
		
		while(l <= r)
		{
			int mid= l + (r-1/2);

			if(array[mid] == x)
			{
				return mid;
			}
			//x is on the right side (greater) of mid
			if(x > array[mid])
			{
				l = mid+1;
			}
			//x is on left side (smaller) of mid
			if(x < array[mid])
			{
				r = mid-1;
			}
			
		}
		return -1;			
	}
	
	public static int recursiveBinearySearch(int[] array, int l, int r, int x)
	{
		int mid= l + (r-1/2);
	
		if(l <= r)
		{
			if(array[mid] == x)
			{
				return mid;
			}
			//x is on the right side (greater) of mid
			if(x > array[mid])
			{
				return recursiveBinearySearch(array,x+1,r, x);
			}
			//x is on left side (smaller) of mid
			if(x < array[mid])
			{
				return recursiveBinearySearch(array, l, r-1, x);
			}
		}
		return -1;

	}
	
	public static void main(String[] argv)
	{
		// Ascending Sorted Array
		int[] A = new int[]{1,3,5,7,8,9,10,21,34};		
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 21)+","+iterativeBinarySearch(A, 0, A.length-1, 21));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 1)+","+iterativeBinarySearch(A, 0, A.length-1, 1));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 34)+","+iterativeBinarySearch(A, 0, A.length-1, 34));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 9)+","+iterativeBinarySearch(A, 0, A.length-1, 9));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 11)+","+iterativeBinarySearch(A, 0, A.length-1, 11));

		
		// Ascending Sorted Array
		A = new int[]{1,3,5,7,8,10,21,34};
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 21)+","+iterativeBinarySearch(A, 0, A.length-1, 21));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 1)+","+iterativeBinarySearch(A, 0, A.length-1, 1));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 34)+","+iterativeBinarySearch(A, 0, A.length-1, 34));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 8)+","+iterativeBinarySearch(A, 0, A.length-1, 8));
		System.out.println(recursiveBinearySearch(A, 0, A.length-1, 9)+","+iterativeBinarySearch(A, 0, A.length-1, 9));
		

		
		
	}

}
