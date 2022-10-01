# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(i) for i in digits]
        res = int("".join(s))  # Join list items using join() method and turn into an integer
        res +=1 #adding a one to the integer

        newList= [] 
        
        string = str(res) #converting the integer into a string
        
        for x in string:
            newList.append(x) #adding each item in string to the new list 
            
        return newList