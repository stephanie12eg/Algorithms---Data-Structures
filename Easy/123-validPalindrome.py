#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# e.g. Input: s = "A man, a plan, a canal: Panama"   
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([t.lower() for t in s if t.isalnum()]) #a method checking if the item is alphanumeric 
        return s[::-1] == s 