package org.abhinav.hackerrank.warmup;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Scanner;

/**
 * @author abhinav
 * https://www.hackerrank.com/challenges/lonely-integer/submissions/code/11113403
 */
public class LonelyInteger {

	static int lonelyinteger(int[] a) {
	       
	      HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
	      
	      for(int i=0; i< a.length; i++)
	      {
	          if(map.containsKey(a[i]))
	          {
	              map.put(a[i],map.get(a[i])+1);
	          }else{
	              map.put(a[i],1);
	          }
	      }
	      
	       Iterator<Entry<Integer, Integer>> item = map.entrySet().iterator();
	       
	       while(item.hasNext()) {
	         Entry<Integer, Integer> me = item.next();
	         if(me.getValue() == 1)
	         {
	             return me.getKey();
	         }
	      }
	      
	      return 0;
	    }
	   public static void main(String[] args) {
	        Scanner in = new Scanner(System.in);
	        int res;
	        
	        int _a_size = Integer.parseInt(in.nextLine());
	        int[] _a = new int[_a_size];
	        int _a_item;
	        String next = in.nextLine();
	        String[] next_split = next.split(" ");
	        
	        for(int _a_i = 0; _a_i < _a_size; _a_i++) {
	            _a_item = Integer.parseInt(next_split[_a_i]);
	            _a[_a_i] = _a_item;
	        }
	        
	        res = lonelyinteger(_a);
	        System.out.println(res);
	 	   in.close();

	    }
	   
	
}
