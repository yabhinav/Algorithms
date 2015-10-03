package org.abhinav.hackerrank.warmup;

import java.util.Scanner;

/**
 * @author abhinav
 * https://www.hackerrank.com/challenges/maximizing-xor/
 * https://www.hackerrank.com/challenges/maximizing-xor/submissions/code/11115185
 */
public class MaximizingXOR {

	
	 /*
	    * Bruteforce method calculate XOR for each combination
	    
	    static int maxXor(int l, int r) {
	        int max = Integer.MIN_VALUE;
	        for(int i = l; i <= r; i++){
	            for(int j= l; j <= r; j++){
	                int tmp = i ^ j;
	                if(tmp>max)
	                    max = tmp;
	            }
	        }
	        return res;
	    }*/
	    
	    /*
	    * Add a 1bit for every bit of the L and R  to get maximum
	    */
	    static int maxXor(int l, int r) {
	        int max = 0;
	        while(l!=r)
	        {
	          l >>= 1;  
	          r >>=1;
	          max = (max <<1) +1;
	        }
	        return max;
	    }

	    public static void main(String[] args) {
	        Scanner in = new Scanner(System.in);
	        int res;
	        int _l;
	        _l = Integer.parseInt(in.nextLine());
	        
	        int _r;
	        _r = Integer.parseInt(in.nextLine());
	        
	        res = maxXor(_l, _r);
	        System.out.println(res);
	        
	    }
}
