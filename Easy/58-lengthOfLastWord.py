# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = list(s.split()) # the split method splits every word in a string into elements in an array. e.g. "hello world " >> [hello, world]
        return len(s[-1]) #finding the length of the last item in the array 
        