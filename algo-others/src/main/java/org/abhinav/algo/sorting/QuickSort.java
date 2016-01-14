package org.abhinav.algo.sorting;

public class QuickSort {

	public static void quickSort(int l, int[] A, int h)
	{
		int i = l;
		int j = h;
		// calculate pivot number, I am taking pivot as middle index number
		int pivot = A[l+(h-l)/2];
		// Divide into two arrays
		while (i <= j) {
			/**
			 * In each iteration, we will identify a number from left side which
			 * is greater then the pivot value, and also we will identify a number
			 * from right side which is less then the pivot value. Once the search
			 * is done, then we exchange both numbers.
			 */
			while (A[i] < pivot) {
				i++;
			}
			while (A[j] > pivot) {
				j--;
			}
			//swap(i, j)
			if (i <= j) {
				int tmp = A[i];
				A[i] = A[j];
				A[j] = tmp;
				
				//move index to next position on both sides
				i++;
				j--;
			}
		}
		// call quickSort() method recursively
		if (l < j)
			quickSort(l, A, j);
		if (i < h)
			quickSort(i,A, h);
	}

	public static void main(String args[]) {
		int[]  A = { 1, 5, 6, 7, 3, 9, 4, 0, 5 };
         quickSort(0, A, A.length-1);
		for (int i = 0; i < A.length; i++) {
			System.out.print(A[i] + "\t");
		}
	}
}
