# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x== 0: # sqrt(0) == 0 
            return 0 
        
        if x == 1: # sqrt(1) == 1
            return 1
        
        i = 1 # the sqrt of each number is inbetween 1 and half of the number e.g. sqrt(36) == 6 which is inbetween 1 and 18. 
        j = x//2
        res = 0  

        while i<=j:
            mid = (i+j)//2
            if mid * mid <= x: #binary search between lowest value 1 and highest value x//2 
                res = mid
                i = mid + 1
            else:
                j = mid - 1
        return int(res) #converting result into an integer to remove demical (truncate)