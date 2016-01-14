package org.abhinav.algo.sorting;

public class BubbleSort {


	
	public static void bubble_srt(int array[]) {
		int m= array.length ,n = array.length;
		int k;
		//Loop n times
		while(m-- >=0 ) {
			//Start from 1 and swap adjacnet elements when i > i+1
			// continue for i = 2 ,3, 4, .... n-1
			for (int i = 0; i < n - 1; i++) {
				k = i + 1;
				if (array[i] > array[k]) {
					swapNumbers(i, k, array);
				}
			}
			printNumbers(array);
		}
	}

	private static void swapNumbers(int i, int j, int[] array) {

		int temp;
		temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}

	private static void printNumbers(int[] input) {

		for (int i = 0; i < input.length; i++) {
			System.out.print(input[i] + ", ");
		}
		System.out.println("\n");
	}

	public static void main(String[] args) {
		int[] input = { 4, 2, 9, 6, 23, 12, 34, 0, 1 };
		bubble_srt(input);

	}
}
