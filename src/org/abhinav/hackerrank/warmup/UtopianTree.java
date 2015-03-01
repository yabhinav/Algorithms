package org.abhinav.hackerrank.warmup;

import java.util.Scanner;

/**
 * @author abhinav
 * https://www.hackerrank.com/challenges/utopian-tree/submissions/code/11115047
 */
public class UtopianTree {

	 public static void main(String[] args) {
	        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
	        
	        Scanner in = new Scanner(System.in);
	        
	        int T = Math.min(10,in.nextInt());
	        
	        int[] a = new int[60];
	        a[0]=1;a[1]=2;
	        for(int i=2;i<60;i++)
	        {           
	          if(i %2 == 0 )
	          {
	            a[i] =  a[i-1]+1;
	          }else{
	              a[i]= 2*a[i-1];
	          }
	        }
	        
	        while(T-- >0)
	        {
	           int N = in.nextInt();
	           if(N<=60)
	           {
	            System.out.println(a[N]);   
	           }else{
	            System.out.println(a[60]); //or preint error
	           }
	        }
	        
	    }
}
