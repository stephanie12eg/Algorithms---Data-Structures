# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The relative order of the elements may be changed.
# if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# example: Input: nums = [0,1,2,2,3,0,4,2], val = 2 
# Output: 5, nums = [0,1,3,0,4,_,_,_]

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        counter = 0 
        
        for i in range (len(nums)):
            
            if nums[i] != val:
                nums[counter] = nums[i]
                counter +=1
                
        return counter 