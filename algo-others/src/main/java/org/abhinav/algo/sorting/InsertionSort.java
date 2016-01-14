package org.abhinav.algo.sorting;


/*
 * Insertion sort iterates through the list by consuming one input element at each repetition, and growing a sorted output list. 
 * On a repetition, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. 
 * It repeats until no input elements remain. 
 */
public class InsertionSort {
	
	public static int[]  insertSort(int[] A )
	{
		for(int i=1; i < A.length ; i++ )
		{
			for(int j=i; j >0 ; j--)
			{
				//swap  //descending order //making sure all elements  including i and below are ordered
				//O(n2) //best for small arrays ..threshold 10-100
				if(A[j] > A[j-1])
				{
					int tmp = A[j-1];
					A[j-1] = A[j];
					A[j]=tmp;
				}
			}
		}
		return A;
	}
	
	public static void main(String args[])
	{
		int[] A = {1,5,6,7,3,9,4,0,5 };
		
		int [] B = insertSort(A);
		
		for(int i=0; i < B.length ; i++)
		{
			System.out.print(B[i] + "\t"  );
		}
	}

}
