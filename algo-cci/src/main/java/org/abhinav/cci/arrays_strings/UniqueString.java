package org.abhinav.cci.arrays_strings;

/**
 * @author abhinav
 *
 *1.1 Implement an algorithm to determine if a string has all unique characters. 
 * What if you cannot use additional data structures?
 */
public class UniqueString {

	public static boolean isUniqueChars(String str) {
		//Check Boundary Conditions
		if (str.length() > 128) {
			return false;
		}

		boolean[] char_set = new boolean[128];//default false
		
		// Go through each character and mark it is visited
		// If already visited its not uniques
		for (int i = 0; i < str.length(); i++) {
			int val = str.charAt(i);
			if (char_set[val]) return false;
			char_set[val] = true;
		}
		
		return true;
	}



	public static void main(String[] args) {
		String[] words = {"abcde", "hello", "apple", "kite", "padle"};
		for (String word : words) {
			System.out.println(word + ": " + isUniqueChars(word) );
		}
	}

}
