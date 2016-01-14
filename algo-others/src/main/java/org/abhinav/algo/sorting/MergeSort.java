package org.abhinav.algo.sorting;

public class MergeSort {

	private int[] A;
	private int[] tmp;
	
	private void sort(int[] A) {
		if(A.length == 0 )
		{
			return;
		}
		
		this.A = A;
		this.tmp = new int[A.length];
		
		mergeSort(0, A.length-1);
	}
	
	private void mergeSort(int l, int h) {
		
		int middle = l + (h-l/2) ;
		
		mergeSort(l, middle);
		mergeSort(middle+1, h);
		
		mergeParts(l, middle, h);

	}	
	
	private void mergeParts(int l, int m, int h)
	{
		for(int i=l; i<=h; i++)
		{
			tmp[i] = A[i];
		}
		
		int i =l , j=m+1,  k = l;
		
		while(i<=m && j<=h )
		{
			if(tmp[i] <= tmp[j])
			{
				A[k] = tmp[i];
				i++;
			} else{
				A[k] = tmp[j];
			}
			k++;
		}
		
		while(i<= m)
		{
			A[k] = tmp[i];
			k++;
			i++;
		}
				
		
	}
	
	public static void main(String args[])
	{
		int[] A = {1,5,6,7,3,9,4,0,5 };
		
	        MergeSort mms = new MergeSort();
	        mms.sort(A);
	        
		for(int i=0; i < A.length ; i++)
		{
			System.out.print(A[i] + "\t"  );
		}
	}


}
