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