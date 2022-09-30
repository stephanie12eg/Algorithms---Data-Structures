# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# return the number of elements remaning after removing duplicates

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1]: # where the element before and current element arent equal is where there is no longer a duplicate. 
                nums[counter] = nums[i] # the counter is 1 meaning the first non-duplicate found after will be inserted into index one, 
                counter += 1 # the next non-duplicate will be inserted into index two as the counter is updated to 2 and so on. 
                
        return counter