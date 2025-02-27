class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size-1,-1,-1):
            if nums[i]==0:
               nums.pop(i)
               nums.append(0)                    
        return nums