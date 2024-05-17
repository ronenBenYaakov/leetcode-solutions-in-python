class Solution(object):
    def productExceptSelf(self, nums):
        n, left, right = len(nums), [1] * len(nums), [1] * len(nums)

        if(n == 0): return []
        if(n == 1) : return [1] * 1
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        res = [0] * n

        for i in range(n):
            res[i] = left[i] * right[i]

        return res

