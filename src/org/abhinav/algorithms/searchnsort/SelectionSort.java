package org.abhinav.algorithms.searchnsort;

import java.util.Arrays;

/*
 * The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part 
 * and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked 
and moved to the sorted subarray.
 */
public class SelectionSort {
	
	public static int[] array ;
	
	public static void selectionSort()
	{
		for(int i=0; i< array.length; i++)
		{
			for(int j=0;j<array.length;j++)
			{
				if(array[i] > array[j]) //Descending order .. reverse it for ascending order
				{
					//swap
					int tmp = array[i];
					array[i] = array[j];
					array[j] = tmp;
				}
			}
		}
	}
	
	public static void main(String[] arg)
	{
		
		array = new int[]{0,5,4,6,7,8,23};
		System.out.print("UnSorted:"+Arrays.toString(array));selectionSort(); System.out.println(" Sorted:" + Arrays.toString(array));
		array = new int[]{23,8,7,6,5,4,0};
		System.out.print("UnSorted:"+Arrays.toString(array));selectionSort(); System.out.println(" Sorted:" + Arrays.toString(array));
		array = new int[]{5,7,23,6,0,8,4};
		System.out.print("UnSorted:"+Arrays.toString(array));selectionSort(); System.out.println(" Sorted:" + Arrays.toString(array));
		array = new int[]{0,00000};
		System.out.print("UnSorted:"+Arrays.toString(array));selectionSort(); System.out.println(" Sorted:" + Arrays.toString(array));
		array = new int[]{9,343,665,234,982,31};
		System.out.print("UnSorted:"+Arrays.toString(array));selectionSort(); System.out.println(" Sorted:" + Arrays.toString(array));
	}

}
