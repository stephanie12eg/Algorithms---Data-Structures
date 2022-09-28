# Given a roman numeral, convert it to an integer.
# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a dictionary that stores the inetger that is equivalent to each roman symbol
        # the if statment is used to check whether the string inputted is going from highest roman symbol to lowest, 
        # if not, a substraction must take place for special cases like IV = 4
        n = len(s)
        symbol = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        integer= 0
        for i in range (n):
            if i+1 < n and symbol[s[i]]< symbol[s[i+1]]:
                integer -= symbol[s[i]]
            else:
                integer += symbol[s[i]]
        return integer 
            
          