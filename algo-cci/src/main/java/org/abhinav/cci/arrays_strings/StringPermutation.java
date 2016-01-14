package org.abhinav.cci.arrays_strings;


/**
 * @author abhinav
 *  1.3 Given two strings, write a method to decide if one is a permutation of the other.
 */
public class StringPermutation {

	public static String sort(String s) {
		char[] content = s.toCharArray();
		java.util.Arrays.sort(content);
		return new String(content);
	}
	
	//Sort the characters in the string so if they are permutations they will be eaul once sorted

	public static boolean permutation(String s, String t) {
		return sort(s).equals(sort(t));
	}
	
	// 
	public static boolean anagram(String s, String t) {
		
		//If length is not same they are permutations
		if (s.length() != t.length())
			return false;
		
		// Store the occurence of char at its int position ..128 being last character ascii value
		int[] letters = new int[128];
		
		int num_unique_chars = 0; //number of unique characters in s
		int num_completed_t = 0; //number of unique characters in t
		
		//Store the s string characters in an array
		char[] s_array = s.toCharArray();
		
		for (char c : s_array) { // count number of each char in s.
			if (letters[c] == 0)
				++num_unique_chars; //maintain unique char count
			++letters[c]; //increment the count/occurence of char c in letters array
		}
		
		//comparing s with t
		for (int i = 0; i < t.length(); ++i) {
			int c = (int) t.charAt(i); //get ascii value 
			
			if (letters[c] == 0) { // Character in t not found in s ..so cant be perm
				return false;
			}
			--letters[c]; //decrement occurence since the char matched once with s_chars
			
			if (letters[c] == 0) { //Means character c cannot occur anymore on t
				++num_completed_t; 
				
				if (num_completed_t == num_unique_chars) { //All the characters are read already  and any extra chars ignored ??
					// its a match if t has been processed completely
					return true;
					//return i == t.length() - 1;
				}
			}
		}
		return false;
	}	
	
	public static void main(String[] args) {
		String[][] pairs = {{"apple", "papel"}, {"carrot", "tarroc"}, {"hello", "llloh"}};
		for (String[] pair : pairs) {
			String word1 = pair[0];
			String word2 = pair[1];
			boolean anagram = permutation(word1, word2);
			System.out.println(word1 + ", " + word2 + ": " + anagram);
			System.out.println(anagram(word1, word2));
		}
	}
}
