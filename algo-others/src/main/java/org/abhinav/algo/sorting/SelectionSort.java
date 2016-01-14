package org.abhinav.algo.sorting;

public class SelectionSort {
	
	public static int[] selectionSort(int[] A)
	{
		// Ascending //Parse the array and place the lowest element of that position
		for(int i=0; i< A.length; i++)
		{
			for(int j=i; j<A.length; ++j)
			{
				if(A[i] > A[j])
				{
					//swap
					int tmp = A[i];
					A[i] = A[j];
					A[j] = tmp;
				}
			}
		}
		
		
		return A;
	}

	public static void main(String args[])
	{
		int[] A = {1,5,6,7,3,9,4,0,5 };
		
		int [] B = selectionSort(A);
		
		for(int i=0; i < B.length ; i++)
		{
			System.out.print(B[i] + "\t"  );
		}
	}
}
