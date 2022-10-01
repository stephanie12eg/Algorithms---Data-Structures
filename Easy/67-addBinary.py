# Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a,2) + int(b,2), "b") # in(,2) changes the string into an integer of base 2, format (,"b") returns format as binary 