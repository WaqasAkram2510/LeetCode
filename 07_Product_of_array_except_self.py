class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        ans = [1]*l
        a = 1
        for i in range(l):
            ans[i] = a
            a *= nums[i]
        b = 1
        for i in range(l-1,-1,-1):
            ans[i] *= b
            b *= nums[i]
        return ans