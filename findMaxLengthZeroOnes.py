class Solution(object):
    def findMaxLengthZeroOnes(self, nums):
        diff, zero, one, res = {} , 0, 0, 0

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one - zero not in diff:
                diff[one - zero] = i

            if one == zero:
                res = one + zero

            else:
                idx = diff[one - zero]
                res = max(res, i - idx)

        return res
