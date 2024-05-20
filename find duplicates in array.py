class Solution(object):
    def findDuplicates(self, nums):
        n, res = len(nums), []

        for i in range(n):
            dest = abs(nums[i]) - 1
            
            if nums[dest] < 0:
                res.append(abs(nums[i]))
            
            nums[dest] *= -1

        return res
            
            
