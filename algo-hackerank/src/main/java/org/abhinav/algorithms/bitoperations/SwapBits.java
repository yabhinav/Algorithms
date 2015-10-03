package org.abhinav.algorithms.bitoperations;

import java.util.Scanner;

/**
 * @author eyalabh
 * How to swap bits at indexes i and j for a 32 bit word/integer
 */
public class SwapBits {
	
	private static int SwapBit(int n, int i, int j) {
		
		//System.out.println(Integer.toBinaryString(n));
		
		//System.out.println(Integer.toBinaryString(1 << i));
		//System.out.println(Integer.toBinaryString(n & (1 << i)));
		int bit_i = (n & (1 << i)) >> i;	// get bit i 
		//System.out.println(Integer.toBinaryString(bit_i));

		//System.out.println("------------------");

		//System.out.println(Integer.toBinaryString(1 << j));
		//System.out.println(Integer.toBinaryString(n & (1 << j)));		
		int bit_j = (n & (1 << j)) >> j;	// get bit j
		//System.out.println(Integer.toBinaryString(bit_j));
	
		//System.out.println("------------------");

		int mask = ~((1 << i) | (1 << j));	// mask to unset bits i and j
		
		//System.out.println(Integer.toBinaryString(mask));

		
		return (n & mask) | (bit_i << j) | (bit_j << i);
		
	}
	
	public static void main(String[] args)
	{
		
		Scanner in = new Scanner(System.in);
		
		 int num = in.nextInt();
		 int i = in.nextInt();
		 int j = in.nextInt();
		 
		 System.out.println(SwapBit(num, i, j));
		
	}

}
