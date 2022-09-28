# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # the input number is converted into a string, then an equality boolean operator, (returning an output of false or true), 
        # is used to check whether the original string and reverse string are equal
        # negative one means that the list is reversed starting from the last element in the string
        return str(x)==str(x)[::-1]
        