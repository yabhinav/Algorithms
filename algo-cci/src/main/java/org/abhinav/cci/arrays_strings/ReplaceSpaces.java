package org.abhinav.cci.arrays_strings;

import org.abhinav.cci.library.*;

/**
 * @author abhinav
 *1.4 Write a method to replace all spaces in a string with'%20'. 
 *You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if imple- menting in Java, please use a character array so that you can perform this opera- tion in place.)
   EXAMPLE
   Input: "Mr John Smith 
   Output: "Mr%20Dohn%20Smith"
 */
public class ReplaceSpaces {
	// Assume string has sufficient free space at the end
	public static void replaceSpaces(char[] str, int length) {
		int spaceCount = 0, index, i = 0;
		
		for (i = 0; i < length; i++) {
			if (str[i] == ' ') {
				spaceCount++;
			}
		}
		
		//new string length is increase by 2 characters more ( ' ' is one char and '%20'is 3 chars)
		index = length + spaceCount * 2; // ( length + spaceCount * 2 + 1  is the length)
		
		str[index] = '\0'; //marking EndofString
		
		//Start from the End
		for (i = length - 1; i >= 0; i--) {
			// If i is space add three chars '%20
			if (str[i] == ' ') {
				str[index - 1] = '0';
				str[index - 2] = '2';
				str[index - 3] = '%';
				index = index - 3;
			} else {
				str[index - 1] = str[i];
				index--;
			}
		}
	}
	
	public static void main(String[] args) {
		String str = "abc d e f";
		char[] arr = new char[str.length() + 3 * 2 + 1];
		for (int i = 0; i < str.length(); i++) {
			arr[i] = str.charAt(i);
		}
		replaceSpaces(arr, str.length());	
		System.out.println("\"" + UtilMethods.charArrayToString(arr) + "\"");
	}

}
