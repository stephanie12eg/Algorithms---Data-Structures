# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap with dictionary 
        storage = {}
        # for loop to iterate through the list, enumerate to gain access to the element at the index in each ieration. 
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in storage:
                storage[num] = i
            else:
                return [storage[diff], i]