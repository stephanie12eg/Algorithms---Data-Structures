# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#decision tree and memoization and dynamic programming, https://youtu.be/Y0lT9Fck7qI

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        for i in range(n - 1): # similar concept to finonacci 
            temp = one
            one = one + two
            two = temp
        return one
