# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
# Example 1: Input: strs = ["flower","flow","flight"] Output: "fl"
# Example 2: Input: strs = ["car","cax","care"] Output: "ca"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #empty string is made and any common characters in all strings are added till longest prefix is reached.
        #storing the list of strings ensures the shortest string is compared to the longest. 
        prefix = ""
        
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix +=x
            else: break
        return prefix