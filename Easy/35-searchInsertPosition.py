# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

#solution not o(log n)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        result = 0
        for i in range(len(nums)):
            
            if target == nums[i]:
                result = i
            elif target == nums[i]+1:
                result = i+1
            elif i+1 < len(nums) and nums[i]< target < nums[i + 1]:
                result = i+1
            elif nums[len(nums)-1] < target:
                result = len(nums)
                
                
        return result

# binary search method, O(log n)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i = 0
        j = len(nums)-1
        floor = 0
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
                floor = i
                
        return floor